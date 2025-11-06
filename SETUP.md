# eBizCard Setup Guide

This guide will help you set up the eBizCard application with one-time access keys managed through GitHub Secrets and deployed on GitHub Pages.

## 🎯 Overview

The system works as follows:
1. One-time access keys are stored as GitHub Secrets (never committed to the repository)
2. During deployment, GitHub Actions generates a `keys.json` file from the secrets
3. The `keys.json` file is included in the GitHub Pages deployment
4. Users access the business card with a one-time key via URL parameter
5. After a key is used, it should be manually removed from GitHub Secrets

## 📋 Prerequisites

- A GitHub account
- A GitHub Personal Access Token (PAT) with `repo` and `workflow` permissions

## 🔧 Initial Setup

### Step 1: Create GitHub Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "eBizCard Key Management")
4. Select the following scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
5. Click "Generate token"
6. **Copy the token** (you won't be able to see it again!)

### Step 2: Add Repository Secrets

1. Go to your repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add the following secrets:

#### Secret 1: `EBIZCARD_PAT_TOKEN`
- **Name**: `EBIZCARD_PAT_TOKEN`
- **Value**: Your GitHub Personal Access Token from Step 1

#### Secret 2: `VALID_KEYS`
- **Name**: `VALID_KEYS`
- **Value**: Comma-separated list of keys (leave empty for now, or add initial keys)
- **Example**: `key1,key2,key3`

### Step 3: Update Configuration

1. Open `admin.html` in your repository
2. Update the following constants:
   ```javascript
   const REPO_OWNER = 'your-github-username'; // Replace with your GitHub username
   const REPO_NAME = 'eBizCard';              // Replace with your repo name
   ```

3. Commit and push the changes

### Step 4: Enable GitHub Pages

1. Go to your repository → Settings → Pages
2. Under "Source", select "GitHub Actions"
3. Save the settings

### Step 5: Deploy

1. Go to Actions tab in your repository
2. Click on "Generate and Deploy with Keys" workflow
3. Click "Run workflow" → "Run workflow"
4. Wait for the deployment to complete

## 🔑 Managing Keys

### Method 1: Using GitHub Actions (Recommended)

#### Generate New Keys

1. Go to Actions → "Manage One-Time Keys"
2. Click "Run workflow"
3. Select action: `add_keys`
4. Enter number of keys to generate (e.g., 5)
5. Click "Run workflow"
6. Check the workflow logs to see the generated keys and URLs

#### Remove a Used Key

1. Go to Actions → "Manage One-Time Keys"
2. Click "Run workflow"
3. Select action: `remove_key`
4. Paste the key to remove
5. Click "Run workflow"

#### List All Keys

1. Go to Actions → "Manage One-Time Keys"
2. Click "Run workflow"
3. Select action: `list_keys`
4. Click "Run workflow"
5. Check the workflow logs to see all current keys

### Method 2: Using the Admin Panel

1. Open `https://your-username.github.io/eBizCard/admin.html`
2. Click "Refresh Keys" to see current keys
3. Use the buttons to trigger GitHub Actions workflows
4. Click on specific keys to remove them

### Method 3: Manual Management

1. Go to Settings → Secrets and variables → Actions
2. Click on `VALID_KEYS` secret
3. Click "Update secret"
4. Edit the comma-separated list of keys
5. Save the secret
6. Manually trigger the "Generate and Deploy with Keys" workflow to redeploy

## 📤 Generating Shareable Links

After generating keys, you can create shareable links in this format:

```
https://your-username.github.io/eBizCard/?key=YOUR_KEY_HERE
```

### Example:
```
https://dcnsakthi.github.io/eBizCard/?key=abc123xyz456
```

Each link can only be used once (in theory - see limitations below).

## ⚠️ Limitations

Since GitHub Pages serves static content, there are some important limitations:

1. **Keys are not automatically deleted after use**: When a user visits a link, the key is validated, but it cannot be automatically removed from the `keys.json` file because it's a static site.

2. **Manual key removal required**: After sharing a key and confirming it was used, you should manually remove it using one of the methods above.

3. **Keys are visible in keys.json**: Anyone who knows to look at `https://your-username.github.io/eBizCard/keys.json` can see the current valid keys. This is a limitation of static hosting.

## 🔒 Security Recommendations

1. **Generate keys only when needed**: Don't generate large batches of keys in advance
2. **Remove keys after use**: Regularly clean up used keys
3. **Monitor key usage**: Check your GitHub Pages analytics to see when links are accessed
4. **Rotate keys regularly**: If you suspect keys have been compromised, remove all keys and generate new ones
5. **Consider key expiration**: You could add timestamp-based validation in `app.js` to expire keys after a certain time

## 🛠️ Customizing the Business Card

Edit the `cardData` object in `app.js`:

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

After making changes, commit and push. The site will automatically redeploy.

## 🐛 Troubleshooting

### Keys not showing up
- Make sure the `VALID_KEYS` secret is set correctly
- Check that the GitHub Actions workflow completed successfully
- Verify that GitHub Pages is enabled and pointing to GitHub Actions

### "Invalid or expired access key" error
- The key might have been removed from `VALID_KEYS`
- The deployment might not have completed yet
- Check the `keys.json` file to verify the key is present

### Workflow fails
- Verify that `EBIZCARD_PAT_TOKEN` secret is set correctly
- Make sure the PAT has `repo` and `workflow` permissions
- Check the workflow logs for specific error messages

## 📚 Files Overview

- `index.html`: Main business card page
- `app.js`: Client-side logic for key validation and card display
- `styles.css`: Styling for the business card
- `admin.html`: Admin panel for key management
- `generator.html`: Old generator (can be removed)
- `keys.json`: Generated during deployment (not in repo)
- `.github/workflows/generate-keys.yml`: Main deployment workflow
- `.github/workflows/manage-keys.yml`: Key management workflow
- `.github/workflows/remove-used-key.yml`: Automatic key removal (triggered via API)

## 🚀 Advanced: Automatic Key Removal

To automatically remove keys after use, you would need to:

1. Set up a serverless function (AWS Lambda, Vercel, etc.)
2. Call that function from `app.js` after successful validation
3. The function would use the GitHub API to update the `VALID_KEYS` secret
4. Trigger a redeployment

This is beyond the scope of a pure GitHub Pages solution but is documented in the `remove-used-key.yml` workflow as a starting point.

## 📞 Support

For issues or questions:
1. Check the workflow logs in the Actions tab
2. Review this documentation
3. Open an issue in the GitHub repository
