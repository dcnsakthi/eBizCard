// eBizCard Application
(function() {
    'use strict';
    
    const elements = {
        loading: document.getElementById('loading'),
        errorMessage: document.getElementById('error-message'),
        errorText: document.getElementById('error-text'),
        cardContainer: document.getElementById('card-container'),
        saveContact: document.getElementById('save-contact')
    };
    
    // Card data (in production, this could be fetched from a server)
    const cardData = {
        name: 'John Doe',
        title: 'Software Engineer',
        email: 'john.doe@example.com',
        phone: '+1 (555) 123-4567',
        company: 'Tech Company Inc.',
        website: 'https://www.example.com'
    };
    
    // Initialize the application
    async function init() {
        // Get the access key from URL parameter
        const urlParams = new URLSearchParams(window.location.search);
        const key = urlParams.get('key');
        
        if (!key) {
            showError('No access key provided. Please use a valid link with a key parameter.');
            return;
        }
        
        // Validate the key
        try {
            const isValid = await validateKey(key);
            
            if (isValid) {
                // Mark key as used
                markKeyAsUsed(key);
                
                // Display the card
                displayCard();
            } else {
                showError('Invalid or expired access key. This key has already been used or does not exist.');
            }
        } catch (error) {
            showError('Error validating access key. Please try again later.');
            console.error('Validation error:', error);
        }
    }
    
    // Validate the access key
    async function validateKey(key) {
        try {
            // Fetch the keys database
            const response = await fetch('keys.json');
            if (!response.ok) {
                throw new Error('Failed to load keys database');
            }
            
            const data = await response.json();
            
            // Check if key exists and is valid
            const keyData = data.keys.find(k => k.key === key);
            
            if (!keyData) {
                return false;
            }
            
            // Check if key has already been used (stored in localStorage)
            const usedKeys = getUsedKeys();
            if (usedKeys.includes(key)) {
                return false;
            }
            
            // Check if key has expired (if expiration date is set)
            if (keyData.expiresAt) {
                const expirationDate = new Date(keyData.expiresAt);
                if (expirationDate < new Date()) {
                    return false;
                }
            }
            
            return true;
        } catch (error) {
            console.error('Error validating key:', error);
            throw error;
        }
    }
    
    // Get list of used keys from localStorage
    function getUsedKeys() {
        const stored = localStorage.getItem('ebizcard_used_keys');
        return stored ? JSON.parse(stored) : [];
    }
    
    // Mark a key as used
    function markKeyAsUsed(key) {
        const usedKeys = getUsedKeys();
        if (!usedKeys.includes(key)) {
            usedKeys.push(key);
            localStorage.setItem('ebizcard_used_keys', JSON.stringify(usedKeys));
        }
    }
    
    // Display the business card
    function displayCard() {
        // Populate card with data
        document.getElementById('card-name').textContent = cardData.name;
        document.getElementById('card-title').textContent = cardData.title;
        document.getElementById('card-email').textContent = cardData.email;
        document.getElementById('card-phone').textContent = cardData.phone;
        document.getElementById('card-company').textContent = cardData.company;
        
        const websiteLink = document.getElementById('card-website');
        websiteLink.textContent = cardData.website;
        websiteLink.href = cardData.website;
        
        // Hide loading and show card
        elements.loading.classList.add('hidden');
        elements.cardContainer.classList.remove('hidden');
    }
    
    // Show error message
    function showError(message) {
        elements.errorText.textContent = message;
        elements.loading.classList.add('hidden');
        elements.errorMessage.classList.remove('hidden');
    }
    
    // Generate vCard and download
    function generateVCard() {
        const vcard = [
            'BEGIN:VCARD',
            'VERSION:3.0',
            `FN:${cardData.name}`,
            `TITLE:${cardData.title}`,
            `ORG:${cardData.company}`,
            `EMAIL:${cardData.email}`,
            `TEL:${cardData.phone}`,
            `URL:${cardData.website}`,
            'END:VCARD'
        ].join('\n');
        
        // Create blob and download
        const blob = new Blob([vcard], { type: 'text/vcard' });
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `${cardData.name.replace(/\s+/g, '_')}.vcf`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
    }
    
    // Event listeners
    elements.saveContact.addEventListener('click', generateVCard);
    
    // Start the application
    init();
})();
