#!/usr/bin/env python3
"""
Generate config.js with credentials from environment variables.
This script is used during GitHub Actions deployment to inject secrets.
"""
import os
import json

# Read environment variables
username = os.environ.get('ADMIN_USERNAME', 'admin')
password = os.environ.get('ADMIN_PASSWORD', 'ChangeThisPassword!2024')

# Use json.dumps to properly escape strings for JavaScript
username_escaped = json.dumps(username)
password_escaped = json.dumps(password)

config_content = f"""// eBizCard Configuration
// Admin authentication credentials for QR code generation
// IMPORTANT: For production use, implement server-side authentication
// This client-side validation is for demonstration purposes only

const CONFIG = {{
    // Admin username for accessing the QR code generator
    ADMIN_AUTH_USER_NAME: {username_escaped},
    
    // Admin password for accessing the QR code generator
    // IMPORTANT: Change this default password to a strong, unique password
    // In production, this should be hashed and validated server-side
    ADMIN_AUTH_SECRET_KEY: {password_escaped}
}};
"""

with open('config.js', 'w') as f:
    f.write(config_content)

print("✓ config.js has been generated successfully with credentials from secrets")
