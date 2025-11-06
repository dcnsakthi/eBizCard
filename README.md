# eBizCard - Electronic Business Card with One-Time Access

A secure, one-time access electronic business card system powered by GitHub Pages and GitHub Secrets.

## 🌟 Features

- **One-time access keys**: Each link can only be used once (manually managed)
- **Secure key storage**: Keys stored as GitHub Secrets, never committed to repository
- **Easy deployment**: Fully hosted on GitHub Pages, no external servers needed
- **Simple management**: Manage keys through GitHub Actions workflows
- **vCard download**: Visitors can save contact information directly to their phone
- **QR Code Support**: Generate QR codes for easy sharing

## 🚀 Quick Start

1. **Fork or clone this repository**

2. **Set up GitHub Secrets**:
   - Go to Settings → Secrets and variables → Actions
   - Create `EBIZCARD_PAT_TOKEN` with your GitHub Personal Access Token
   - Create `VALID_KEYS` with comma-separated keys (or leave empty)

3. **Update admin.html**:
   - Edit `REPO_OWNER` and `REPO_NAME` constants

4. **Enable GitHub Pages**:
   - Go to Settings → Pages
   - Source: GitHub Actions

5. **Deploy**:
   - Go to Actions → "Generate and Deploy with Keys"
   - Click "Run workflow"

For detailed setup instructions, see [SETUP.md](SETUP.md)

## 🔑 Managing Keys

### Generate Keys
1. Go to Actions → "Manage One-Time Keys"
2. Run workflow with action: `add_keys`
3. Specify number of keys to generate

### Remove Keys
1. Go to Actions → "Manage One-Time Keys"
2. Run workflow with action: `remove_key`
3. Paste the key to remove

### Admin Panel
Access the admin panel at: `https://your-username.github.io/eBizCard/admin.html`

## 📤 Share Your Card

After generating keys, share links in this format:
```
https://your-username.github.io/eBizCard/?key=YOUR_KEY_HERE
```

## 🎨 Customization

Edit `app.js` to update your business card information:

```javascript
const cardData = {
    name: 'Your Name',
    title: 'Your Title',
    email: 'your.email@example.com',
    phone: '+1 (555) 123-4567',
    company: 'Your Company',
    website: 'https://www.your-website.com'
};
```

### Styling

Edit `styles.css` to customize colors, fonts, and layout.

## 📁 Project Structure

```
eBizCard/
├── .github/
│   └── workflows/
│       ├── generate-keys.yml      # Main deployment workflow
│       ├── manage-keys.yml        # Key management workflow
│       └── remove-used-key.yml    # Automatic key removal
├── index.html                     # Business card page
├── app.js                         # Client-side logic
├── styles.css                     # Styling
├── admin.html                     # Admin panel
├── generator.html                 # Legacy generator
├── qrcode.min.js                 # QR code library
├── SETUP.md                       # Detailed setup guide
└── README.md                      # This file
```

## ⚠️ Important Notes

- Keys are **not automatically removed** after use (GitHub Pages limitation)
- You must manually remove used keys via GitHub Actions
- The `keys.json` file is public - anyone can see valid keys
- This is best for controlled distribution where you can track usage

## 🔒 Security Considerations

1. Generate keys only when needed
2. Remove keys immediately after use
3. Monitor key usage through GitHub Pages analytics
4. Rotate keys regularly if needed
5. Consider adding expiration timestamps for additional security

## 📝 License

See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
