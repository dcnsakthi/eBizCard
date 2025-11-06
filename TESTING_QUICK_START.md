# 🧪 Local Testing - Quick Start

## Problem You're Experiencing

You're seeing these errors because you're trying to use the **production files** (`admin.html`, `index.html`) locally, but they need secrets injected by GitHub Actions during deployment.

## ✅ Solution: Use Test Files

### For Admin Panel Testing

Use `admin.test.html` instead of `admin.html`:

```bash
# Start server
python3 -m http.server 8000

# Open in browser
http://localhost:8000/admin.test.html
```

**Login Credentials:**
- Username: `admin`
- Password: `test123`

You should now see:
1. ✅ Login screen with yellow "TEST MODE" banner
2. ✅ Credentials pre-filled
3. ✅ After login: Admin panel with 3 test keys
4. ✅ No errors!

### For Business Card Testing

Use `index.test.html` instead of `index.html`:

```bash
# Test with valid key
http://localhost:8000/index.test.html?key=ikFqxDvBilungTDv2k7R

# Test with invalid key
http://localhost:8000/index.test.html?key=wrongkey
```

## 📁 Files Comparison

| File | Purpose | Works Locally? | When to Use |
|------|---------|----------------|-------------|
| `admin.html` | Production | ❌ No | After GitHub deployment |
| `admin.test.html` | Testing | ✅ Yes | Local development |
| `index.html` | Production | ❌ No | After GitHub deployment |
| `index.test.html` | Testing | ✅ Yes | Local development |

## 🔍 What's the Difference?

### Production Files (admin.html, index.html)
```javascript
// Placeholders - replaced during GitHub Actions deployment
const ADMIN_CREDENTIALS = {
    username: 'ADMIN_AUTH_USER_NAME_PLACEHOLDER', // ❌ Not defined locally
    password: 'ADMIN_AUTH_SECRET_KEY_PLACEHOLDER'  // ❌ Not defined locally
};

// No VALID_KEYS_FROM_SECRET defined ❌
// This causes: "Error loading keys: VALID_KEYS_FROM_SECRET is undefined"
```

### Test Files (admin.test.html, index.test.html)
```javascript
// Real test values - work immediately ✅
const ADMIN_CREDENTIALS = {
    username: 'admin',
    password: 'test123'
};

// Test keys embedded ✅
const VALID_KEYS_FROM_SECRET = "ikFqxDvBilungTDv2k7R,testkey123,anotherkey456";
```

## 🎯 Summary

**Your Error:** "Error loading keys: Failed to load keys" + No auth screen
**Cause:** Using production files locally without deployed secrets
**Fix:** Use `admin.test.html` and `index.test.html` for local testing

**Quick Commands:**
```bash
# Start server
python3 -m http.server 8000

# Test admin (with auth)
# Browser: http://localhost:8000/admin.test.html

# Test business card
# Browser: http://localhost:8000/index.test.html?key=ikFqxDvBilungTDv2k7R
```

That's it! 🎉
