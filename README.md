# eBizCard
eBizCard for Secure Contact Exchange with One-Time Access Keys

## Features

- 🔒 **Secure One-Time Access**: Each access key can only be used once
- 📱 **QR Code Support**: Generate QR codes for easy NFC/QR scanning
- 💼 **Professional Display**: Clean, modern business card presentation
- 💾 **vCard Export**: Save contact information directly to phone/computer
- 🌐 **GitHub Pages Hosted**: Fully static, no server required

## How It Works

1. **Key Generation**: Use the generator tool to create unique, secure access keys
2. **QR Code Creation**: Each key gets a unique URL and QR code
3. **One-Time Access**: When someone scans the QR code or visits the URL, they can view your contact information
4. **Automatic Expiration**: After the first access, the key is marked as used and cannot be reused

## Quick Start

### For Users (Viewing a Business Card)

Simply scan the QR code or click the link you received. You'll see the contact information and can save it to your device.

### For Card Owners (Setting Up Your Card)

1. **Edit Contact Information**: Update `app.js` with your details:
   ```javascript
   const cardData = {
       name: 'Your Name',
       title: 'Your Title',
       email: 'your.email@example.com',
       phone: '+1 (555) 123-4567',
       company: 'Your Company',
       website: 'https://yourwebsite.com'
   };
   ```

2. **Configure Admin Authentication**: Set up GitHub repository secrets for secure authentication:
   - Go to your repository Settings → Secrets and variables → Actions
   - Add two repository secrets:
     - `ADMIN_AUTH_USER_NAME`: Your admin username
     - `ADMIN_AUTH_SECRET_KEY`: Your secure admin password
   
   **Note**: The secrets are automatically injected into `config.js` during deployment via GitHub Actions. The default values in the repository are only used for local development.

3. **Generate Access Keys**: Open `generator.html` in your browser
   - You will be prompted to enter admin credentials
   - Enter the username and password you configured in GitHub Secrets
   - Specify how many keys you need
   - Click "Generate Keys"
   - Download the `keys.json` file
   - Replace the existing `keys.json` with your generated file

4. **Deploy to GitHub Pages**:
   - Push your changes to GitHub
   - Enable GitHub Pages in repository settings
   - Select the main/master branch as the source
   - The GitHub Actions workflow will automatically inject your secrets during deployment

5. **Share Your Card**:
   - Download the QR codes from the generator
   - Print them on business cards, stickers, or NFC tags
   - Share the URLs directly via email or messaging

## Security Features

- **Admin Authentication**: QR code generation is protected by Basic Authentication using GitHub Secrets
- **Secure Credential Management**: Admin credentials are stored as GitHub repository secrets and injected during deployment
- **One-Time Use**: Keys are marked as used after first access (stored in localStorage)
- **Cryptographically Secure**: Keys are generated using `crypto.getRandomValues()`
- **No Server Required**: Fully client-side validation for privacy
- **Optional Expiration**: Support for time-based key expiration

## Project Structure

```
├── index.html          # Main business card display page
├── app.js             # Application logic and key validation
├── styles.css         # Styling for the business card
├── generator.html     # Key generator tool (admin access only)
├── config.js          # Admin authentication configuration
├── keys.json          # Database of valid access keys
└── _config.yml        # GitHub Pages configuration
```

## Customization

### Styling

Edit `styles.css` to customize colors, fonts, and layout. The default theme uses a purple gradient, but you can easily change it:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Card Fields

Add or remove fields by editing the HTML in `index.html` and the data structure in `app.js`.

## Limitations

- Keys are validated client-side using localStorage, which can be cleared by the user
- For production use, consider implementing server-side key validation
- The `keys.json` file is public, so keys can be discovered (though still single-use)

## Advanced Usage

### Server-Side Integration

For enhanced security, you can integrate with a backend service:

1. Store keys in a database instead of `keys.json`
2. Validate and mark keys as used server-side
3. Use an API endpoint instead of localStorage

### NFC Tags

1. Generate access keys using the generator
2. Write the URLs to NFC tags using an NFC writing app
3. Place NFC tags on physical business cards or stickers

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
