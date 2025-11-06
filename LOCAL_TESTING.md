# Local Testing Guide

Since the keys are now injected from GitHub Secrets during deployment, you need to use test files for local development.

## 🚀 Quick Start

### Option 1: Use Pre-configured Test Files (RECOMMENDED)

```bash
# Start local server
python3 -m http.server 8000

# Open in browser
# Admin Panel: http://localhost:8000/admin.test.html
# Business Card: http://localhost:8000/index.test.html?key=ikFqxDvBilungTDv2k7R
```

**Test Credentials:**
- **Username:** `admin`
- **Password:** `test123`

**Test Keys:**
- `ikFqxDvBilungTDv2k7R`
- `testkey123`
- `anotherkey456`

### Option 2: Command Line Testing

```bash
# Start server
cd /workspaces/eBizCard
python3 -m http.server 8000

# In another terminal, test the pages
curl http://localhost:8000/index.test.html?key=ikFqxDvBilungTDv2k7R
```

## 📁 Test Files Available

### 1. `admin.test.html` ✅
- Full admin panel with authentication
- Pre-configured credentials (admin/test123)
- Test keys embedded
- Login screen works
- Key listing works
- Perfect for testing admin functionality

### 2. `index.test.html` ✅
- Business card page
- Test keys embedded
- Works with URL parameter: `?key=XXX`
- Perfect for testing key validation

## 🧪 Testing Scenarios

### Test Admin Login
```
1. Open: http://localhost:8000/admin.test.html
2. Should see login screen with yellow test banner
3. Credentials pre-filled: admin / test123
4. Click "Login"
5. Should see admin panel with 3 test keys
```

### Test Business Card Access
```
1. Valid key:
   http://localhost:8000/index.test.html?key=ikFqxDvBilungTDv2k7R
   → Should show business card

2. Invalid key:
   http://localhost:8000/index.test.html?key=invalidkey
   → Should show "Access Denied" error

3. No key:
   http://localhost:8000/index.test.html
   → Should show "No access key provided" error
```

### Test Admin Logout
```
1. Login to admin panel
2. Click "Logout" button
3. Should return to login screen
4. Session cleared
```

## ⚠️ Important Notes

### For Production Files (admin.html, index.html)

These files will **NOT work locally** because they need secrets injected by GitHub Actions:

```html
<!-- These placeholders are replaced during deployment -->
<script>const VALID_KEYS_FROM_SECRET = "PLACEHOLDER";</script>

const ADMIN_CREDENTIALS = {
    username: 'ADMIN_AUTH_USER_NAME_PLACEHOLDER',
    password: 'ADMIN_AUTH_SECRET_KEY_PLACEHOLDER'
};
```

### Always Use .test.html Files Locally

| File | Purpose | Works Locally? |
|------|---------|----------------|
| `index.html` | Production | ❌ No (needs deployment) |
| `index.test.html` | Testing | ✅ Yes |
| `admin.html` | Production | ❌ No (needs deployment) |
| `admin.test.html` | Testing | ✅ Yes |

## 🔧 Customizing Test Files

### Add Your Own Test Keys

Edit `index.test.html` or `admin.test.html`:

```html
<!-- Change this line -->
<script>const VALID_KEYS_FROM_SECRET = "yourkey1,yourkey2,yourkey3";</script>
```

### Change Test Credentials

Edit `admin.test.html`:

```javascript
const ADMIN_CREDENTIALS = {
    username: 'yourusername',
    password: 'yourpassword'
};
```

**Remember:** These are test files only. Don't commit real credentials!

## 📦 Production Deployment

In production, the workflow injects real values:

```yaml
# .github/workflows/generate-keys.yml
env:
  VALID_KEYS: ${{ secrets.VALID_KEYS }}
  ADMIN_AUTH_USER_NAME: ${{ secrets.ADMIN_AUTH_USER_NAME }}
  ADMIN_AUTH_SECRET_KEY: ${{ secrets.ADMIN_AUTH_SECRET_KEY }}
```

After deployment, production URLs work:
```
https://dcnsakthi.github.io/eBizCard/admin.html
https://dcnsakthi.github.io/eBizCard/?key=REAL_KEY
```

## 🐛 Troubleshooting

### "Error loading keys: VALID_KEYS_FROM_SECRET is undefined"
- ✅ Use `admin.test.html` instead of `admin.html` for local testing

### "Basic auth screen not showing"
- ✅ Use `admin.test.html` which has auth pre-configured
- ✅ Make sure you're opening the file via http://localhost, not file://

### "Invalid or expired access key"
- ✅ Make sure you're using one of the test keys
- ✅ Check the URL has `?key=` parameter
- ✅ Use `index.test.html` not `index.html`

### Can't see login screen
- ✅ Clear your browser cache/session storage
- ✅ Open in incognito/private window
- ✅ Check console for JavaScript errors (F12)

## 📝 Development Workflow

1. **Local Development:**
   ```bash
   # Use .test.html files
   python3 -m http.server 8000
   # Test at http://localhost:8000/admin.test.html
   ```

2. **Before Committing:**
   ```bash
   # Make sure .test.html files are in .gitignore
   git status
   # Should NOT show *.test.html files
   ```

3. **Production Testing:**
   ```bash
   # After deployment via GitHub Actions
   # Test at https://dcnsakthi.github.io/eBizCard/admin.html
   ```

## ✅ Quick Verification

Run this to verify your setup:

```bash
# Check test files exist
ls -la *.test.html

# Should see:
# admin.test.html
# index.test.html

# Start server and test
python3 -m http.server 8000 &
sleep 1
curl -s http://localhost:8000/admin.test.html | grep "TEST MODE"
# Should output: "TEST MODE"
```

---

**Summary:**
- 🟢 Use `.test.html` files for local development
- 🔴 Production files (`.html`) only work after GitHub Actions deployment
- 🔑 Test credentials: admin/test123
- 🎯 Test keys: ikFqxDvBilungTDv2k7R, testkey123, anotherkey456

