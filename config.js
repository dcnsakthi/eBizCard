// eBizCard Configuration
// Admin authentication credentials for QR code generation
// IMPORTANT: For production use, implement server-side authentication
// This client-side validation is for demonstration purposes only

const CONFIG = {
    // Admin username for accessing the QR code generator
    ADMIN_AUTH_USER_NAME: 'admin',
    
    // Admin password for accessing the QR code generator
    // In production, this should be hashed and validated server-side
    ADMIN_AUTH_SECRET_KEY: 'secure_password_123'
};
