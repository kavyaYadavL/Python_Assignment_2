/* ============================================
   Chat UI - JavaScript Functionality
   CampusPe Gen AI Assignment
   ============================================ */

$(document).ready(function () {

    /* ============================================
       DOM Elements
       ============================================ */

    const chatBox = $("#chatBox");
    const input = $("#messageInput");
    const sendBtn = $("#sendBtn");
    const attachBtn = $("#attachBtn");
    const typing = $("#typing");
    const welcomeScreen = $(".welcome-screen");
    const sidebar = $(".sidebar");
    const overlay = $("#overlay");
    const menuBtn = $("#menuBtn");
    const newChatBtn = $("#newChatBtn");

    /* ============================================
       Configuration & Variables
       ============================================ */

    // Sample AI responses
    const responses = [
        "That's interesting! Tell me more.",
        "I can definitely help with that! 😊",
        "Good question! Let me think about that...",
        "Nice! Keep the ideas coming!",
        "I like where you're going with this!",
        "That makes sense. Here's what I think...",
        "Absolutely, I can assist with that.",
        "Interesting perspective! Let me elaborate..."
    ];

    // Track if first message has been sent
    let hasFirstMessage = false;

    /* ============================================
       Utility Functions
       ============================================ */

    /**
     * Add a message to the chat
     * @param {string} text - Message content
     * @param {string} sender - "user" or "bot"
     */
    function addMessage(text, sender) {
        // Validate input
        if (!text || text.trim() === "") return;

        // Get current time in HH:MM format
        const time = new Date().toLocaleTimeString([], {
            hour: '2-digit',
            minute: '2-digit',
            hour12: true
        });

        // Determine sender name
        const senderName = sender === "user" ? "You" : "Assistant";

        // Create message HTML
        const msg = `
            <div class="message ${sender}">
                <div class="msg-header">
                    <span>${senderName}</span>
                    <small>${time}</small>
                </div>
                <div>${escapeHtml(text)}</div>
            </div>
        `;

        // Add message to chat
        chatBox.append(msg);

        // Auto-scroll to bottom
        scrollToBottom();
    }

    /**
     * Escape HTML to prevent injection
     * @param {string} text - Text to escape
     * @returns {string} Escaped text
     */
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    /**
     * Auto-scroll chat to bottom
     */
    function scrollToBottom() {
        chatBox.animate({
            scrollTop: chatBox[0].scrollHeight
        }, 300);
    }

    /**
     * Show typing indicator
     */
    function showTypingIndicator() {
        typing.removeClass("d-none");
        scrollToBottom();
    }

    /**
     * Hide typing indicator
     */
    function hideTypingIndicator() {
        typing.addClass("d-none");
    }

    /**
     * Get random AI response
     * @returns {string} Random response from array
     */
    function getRandomResponse() {
        return responses[Math.floor(Math.random() * responses.length)];
    }

    /**
     * Simulate bot typing and response
     */
    function botReply() {
        showTypingIndicator();

        // Simulate delay (1-2 seconds)
        const delay = 1000 + Math.random() * 1000;

        setTimeout(() => {
            hideTypingIndicator();

            // Get random response
            const reply = getRandomResponse();
            addMessage(reply, "bot");

        }, delay);
    }

    /**
     * Send message function
     */
    function sendMessage() {
        const text = input.val().trim();

        // Prevent empty messages
        if (text === "") return;

        // Add user message
        addMessage(text, "user");

        // Clear input and reset height
        input.val("").trigger('input');

        // Hide welcome screen on first message
        if (!hasFirstMessage) {
            welcomeScreen.fadeOut(300);
            hasFirstMessage = true;
        }

        // Get bot reply after slight delay
        setTimeout(() => {
            botReply();
        }, 300);
    }

    /**
     * Auto-resize textarea based on content
     */
    function autoResizeTextarea() {
        // Reset height to auto
        input[0].style.height = "auto";

        // Get scroll height
        const scrollHeight = input[0].scrollHeight;

        // Set new height (max 120px)
        const newHeight = Math.min(scrollHeight, 120);
        input[0].style.height = newHeight + "px";
    }

    /**
     * Update send button state
     */
    function updateSendButtonState() {
        const hasText = input.val().trim() !== "";
        sendBtn.prop("disabled", !hasText);
    }

    /**
     * Toggle mobile sidebar
     */
    function toggleSidebar() {
        sidebar.toggleClass("active");
        overlay.toggleClass("active");
    }

    /**
     * Close mobile sidebar
     */
    function closeSidebar() {
        sidebar.removeClass("active");
        overlay.removeClass("active");
    }

    /* ============================================
       Event Listeners - Input Area
       ============================================ */

    /**
     * Input event - auto-resize and button state
     */
    input.on("input", function () {
        autoResizeTextarea();
        updateSendButtonState();
    });

    /**
     * Keypress event - Handle Enter and Shift+Enter
     */
    input.on("keypress", function (e) {
        // Enter without Shift = Send message
        if (e.which === 13 && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
        // Shift+Enter = New line (default behavior)
    });

    /**
     * Send button click
     */
    sendBtn.on("click", function (e) {
        e.preventDefault();
        sendMessage();
    });

    /**
     * Attach button click (placeholder)
     */
    attachBtn.on("click", function (e) {
        e.preventDefault();
        alert("File attachment feature coming soon! 📎");
    });

    /* ============================================
       Event Listeners - Suggestion Cards
       ============================================ */

    /**
     * Suggestion card click
     */
    $(document).on("click", ".suggestion-card", function (e) {
        e.preventDefault();

        // Get card text
        const cardTitle = $(this).find(".card-title").text();
        const cardDescription = $(this).find(".card-description").text();

        // Create message from card
        const message = `${cardTitle}: ${cardDescription}`;

        // Set input value
        input.val(message);

        // Trigger input event for auto-resize
        input.trigger("input");

        // Focus input
        input.focus();

        // Update button state
        updateSendButtonState();

        // Optional: Auto-send after delay
        // setTimeout(() => { sendMessage(); }, 300);
    });

    /* ============================================
       Event Listeners - Mobile Menu
       ============================================ */

    /**
     * Hamburger menu button click
     */
    menuBtn.on("click", function (e) {
        e.preventDefault();
        toggleSidebar();
    });

    /**
     * Overlay click - close sidebar
     */
    overlay.on("click", function (e) {
        e.preventDefault();
        closeSidebar();
    });

    /**
     * Sidebar item click - close menu
     */
    $(document).on("click", ".history-item", function () {
        closeSidebar();
    });

    /* ============================================
       Event Listeners - New Chat
       ============================================ */

    /**
     * New Chat button click
     */
    newChatBtn.on("click", function (e) {
        e.preventDefault();

        // Clear all messages
        chatBox.html("");
        typing.addClass("d-none");

        // Show welcome screen
        welcomeScreen.show();
        hasFirstMessage = false;

        // Reset input
        input.val("").trigger("input");
        input.focus();

        // Scroll to top
        chatBox.scrollTop(0);

        // Close sidebar on mobile
        if ($(window).width() < 768) {
            closeSidebar();
        }
    });

    /* ============================================
       Initialization
       ============================================ */

    /**
     * Initialize on page load
     */
    function init() {
        // Focus input on load
        input.focus();

        // Update button state
        updateSendButtonState();

        // Add some initial welcome messages (optional)
        // You can remove this if you want only the welcome screen

        // Log initialization
        console.log("Chat UI initialized successfully! 🚀");
    }

    // Run initialization
    init();

    /* ============================================
       Keyboard Shortcuts (Optional)
       ============================================ */

    /**
     * Global keyboard shortcuts
     */
    $(document).on("keydown", function (e) {
        // Ctrl/Cmd + L to focus input
        if ((e.ctrlKey || e.metaKey) && e.key === 'l') {
            e.preventDefault();
            input.focus();
        }

        // Escape to close mobile menu
        if (e.key === 'Escape') {
            if (sidebar.hasClass("active")) {
                closeSidebar();
            }
        }
    });

    /* ============================================
       Responsive Behavior
       ============================================ */

    /**
     * Handle window resize
     */
    $(window).on("resize", function () {
        // Close sidebar on large screens
        if ($(window).width() >= 768) {
            closeSidebar();
        }
    });

    /* ============================================
       Console Messages (Development)
       ============================================ */

    // Helpful console logs for debugging
    console.log("Chat UI - CampusPe Assignment");
    console.log("═".repeat(50));
    console.log("Keyboard Shortcuts:");
    console.log("• Ctrl/Cmd + L : Focus message input");
    console.log("• Escape : Close mobile menu");
    console.log("═".repeat(50));

});

/* ============================================
   Additional Utility Functions (Global)
   ============================================ */

/**
 * Format timestamp
 */
function formatTime(date) {
    return date.toLocaleTimeString([], {
        hour: '2-digit',
        minute: '2-digit'
    });
}

/**
 * Check if device is mobile
 */
function isMobile() {
    return $(window).width() < 768;
}