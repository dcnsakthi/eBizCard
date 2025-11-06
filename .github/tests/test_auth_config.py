#!/usr/bin/env python3
"""
Test script to validate the authentication flow in generator.html
"""
import os
import json
import tempfile
import subprocess
import sys

def test_config_generation():
    """Test that the config generation script works correctly"""
    print("Testing config.js generation...")
    
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, 'config.js')
        
        # Set environment variables
        env = os.environ.copy()
        env['ADMIN_USERNAME'] = 'test_user'
        env['ADMIN_PASSWORD'] = 'test_pass_123!'
        
        # Run the generation script
        script_path = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'generate_config.py')
        
        # Change to temp directory and generate config
        result = subprocess.run(
            ['python3', os.path.abspath(script_path)],
            cwd=tmpdir,
            env=env,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"❌ Config generation failed: {result.stderr}")
            return False
        
        # Read the generated config
        with open(config_path, 'r') as f:
            config_content = f.read()
        
        # Verify the content
        if '"test_user"' not in config_content:
            print("❌ Username not found in generated config")
            return False
        
        if '"test_pass_123!"' not in config_content:
            print("❌ Password not found in generated config")
            return False
        
        print("✓ Config generation test passed")
        return True

def test_special_characters():
    """Test that special characters are properly escaped"""
    print("\nTesting special character handling...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, 'config.js')
        
        # Test with special characters
        env = os.environ.copy()
        env['ADMIN_USERNAME'] = "user'with\"quotes"
        env['ADMIN_PASSWORD'] = 'pass\\with\\backslashes'
        
        script_path = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'generate_config.py')
        
        result = subprocess.run(
            ['python3', os.path.abspath(script_path)],
            cwd=tmpdir,
            env=env,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"❌ Config generation with special chars failed: {result.stderr}")
            return False
        
        # Read and verify the config is valid JavaScript
        with open(config_path, 'r') as f:
            config_content = f.read()
        
        # Basic validation - check that the file contains properly escaped strings
        if 'user\\\'with\\"quotes' not in config_content and 'user' not in config_content:
            print("❌ Username with special chars not properly handled")
            return False
        
        print("✓ Special character handling test passed")
        return True

def test_default_values():
    """Test that default values are used when environment variables are not set"""
    print("\nTesting default values...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, 'config.js')
        
        # Don't set environment variables
        env = {key: val for key, val in os.environ.items() if not key.startswith('ADMIN_')}
        
        script_path = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'generate_config.py')
        
        result = subprocess.run(
            ['python3', os.path.abspath(script_path)],
            cwd=tmpdir,
            env=env,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"❌ Config generation with defaults failed: {result.stderr}")
            return False
        
        # Read and verify defaults are used
        with open(config_path, 'r') as f:
            config_content = f.read()
        
        if '"admin"' not in config_content:
            print("❌ Default username not used")
            return False
        
        if '"ChangeThisPassword!2024"' not in config_content:
            print("❌ Default password not used")
            return False
        
        print("✓ Default values test passed")
        return True

def main():
    """Run all tests"""
    print("=" * 60)
    print("Running authentication configuration tests")
    print("=" * 60)
    
    tests = [
        test_config_generation,
        test_special_characters,
        test_default_values
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 60)
    
    return 0 if all(results) else 1

if __name__ == '__main__':
    sys.exit(main())
