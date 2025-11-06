# Local Testing Guide

Since the keys are now injected from GitHub Secrets during deployment, you need to set up test keys for local development.

## Option 1: Use index.test.html

Use the `index.test.html` file which has test keys pre-configured:

```bash
# Start local server
python3 -m http.server 8000

# Open in browser
http://localhost:8000/index.test.html?key=ikFqxDvBilungTDv2k7R
```

Test keys in `index.test.html`:
- `ikFqxDvBilungTDv2k7R`
- `testkey123`
- `anotherkey456`

## Option 2: Temporarily Modify index.html

Add this line before `<script src="app.js"></script>` in `index.html`:

```html
<script>const VALID_KEYS_FROM_SECRET = "yourkey1,yourkey2,yourkey3";</script>
<script src="app.js"></script>
```

**Important**: Don't commit this change! It's for local testing only.

## Option 3: Create admin.test.html

For testing the admin panel locally:

1. Copy `admin.html` to `admin.test.html`
2. Replace the placeholders:
   ```javascript
   const ADMIN_CREDENTIALS = {
       username: 'admin',  // Change to your test username
       password: 'test123'  // Change to your test password
   };
   ```
3. Add test keys before the closing `</body>`:
   ```html
   <script>const VALID_KEYS_FROM_SECRET = "key1,key2,key3";</script>
   ```

## Production Deployment

In production, these values are automatically injected from GitHub Secrets:

- `VALID_KEYS` → Injected as `VALID_KEYS_FROM_SECRET`
- `ADMIN_AUTH_USER_NAME` → Injected into admin credentials
- `ADMIN_AUTH_SECRET_KEY` → Injected into admin credentials

The GitHub Actions workflow handles this automatically during deployment.

## Testing URLs

### Local:
```
http://localhost:8000/index.test.html?key=ikFqxDvBilungTDv2k7R
http://localhost:8000/admin.test.html
```

### Production:
```
https://dcnsakthi.github.io/eBizCard/?key=YOUR_ACTUAL_KEY
https://dcnsakthi.github.io/eBizCard/admin.html
```

## Important Notes

- Never commit files with actual keys or credentials
- Use `.test.html` files for local development
- The `.test.html` files should be in `.gitignore`
- Production files get secrets injected during GitHub Actions deployment
