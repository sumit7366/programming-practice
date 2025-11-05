// Code Editor Integration with JDoodle API
class CodeEditor {
    constructor() {
        this.editors = new Map();
        this.init();
    }

    init() {
        // Initialize code editors for all code blocks
        this.initializeCodeBlocks();
        this.setupRunButtons();
    }

    initializeCodeBlocks() {
        document.querySelectorAll('pre code.language-c').forEach((block, index) => {
            const container = this.createEditorContainer(block, index);
            block.parentNode.replaceChild(container, block);
        });
    }

    createEditorContainer(originalBlock, index) {
        const container = document.createElement('div');
        container.className = 'code-editor-container mb-3';
        
        const toolbar = document.createElement('div');
        toolbar.className = 'code-toolbar bg-secondary text-white p-2 rounded-top d-flex justify-content-between align-items-center';
        
        const title = document.createElement('span');
        title.className = 'fw-bold';
        title.textContent = 'C Code Editor';
        
        const runButton = document.createElement('button');
        runButton.className = 'btn btn-sm btn-success run-code-btn';
        runButton.innerHTML = '<i class="fas fa-play me-1"></i> Run Code';
        runButton.dataset.editorId = `editor-${index}`;
        
        toolbar.appendChild(title);
        toolbar.appendChild(runButton);
        
        const editorArea = document.createElement('div');
        editorArea.className = 'editor-area';
        
        const textarea = document.createElement('textarea');
        textarea.className = 'form-control code-textarea font-monospace';
        textarea.rows = 10;
        textarea.value = originalBlock.textContent;
        textarea.id = `editor-${index}`;
        
        const outputArea = document.createElement('div');
        outputArea.className = 'output-area mt-2';
        outputArea.innerHTML = `
            <div class="output-header bg-dark text-white p-2 rounded-top">
                <span class="fw-bold">Output</span>
            </div>
            <div class="output-content bg-light text-dark p-3 rounded-bottom" id="output-${index}">
                <em class="text-muted">Click "Run Code" to see the output</em>
            </div>
        `;
        
        editorArea.appendChild(textarea);
        editorArea.appendChild(outputArea);
        
        container.appendChild(toolbar);
        container.appendChild(editorArea);
        
        // Store editor reference
        this.editors.set(`editor-${index}`, {
            textarea: textarea,
            output: outputArea.querySelector('.output-content')
        });
        
        return container;
    }

    setupRunButtons() {
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('run-code-btn') || 
                e.target.closest('.run-code-btn')) {
                const button = e.target.classList.contains('run-code-btn') ? 
                    e.target : e.target.closest('.run-code-btn');
                const editorId = button.dataset.editorId;
                this.executeCode(editorId);
            }
        });
    }

    async executeCode(editorId) {
        const editor = this.editors.get(editorId);
        if (!editor) return;

        const code = editor.textarea.value;
        const outputElement = editor.output;
        
        // Show loading state
        outputElement.innerHTML = '<div class="text-center"><div class="spinner-border spinner-border-sm me-2"></div>Running code...</div>';
        
        try {
            // Using JDoodle Compiler API (you'll need to sign up for free credentials)
            const response = await this.callJDoodleAPI(code);
            
            if (response.output) {
                outputElement.innerHTML = `
                    <div class="output-success">
                        <strong class="text-success">Execution Successful:</strong>
                        <pre class="mt-2 mb-0">${this.escapeHtml(response.output)}</pre>
                    </div>
                `;
            } else if (response.error) {
                outputElement.innerHTML = `
                    <div class="output-error">
                        <strong class="text-danger">Execution Error:</strong>
                        <pre class="mt-2 mb-0 text-danger">${this.escapeHtml(response.error)}</pre>
                    </div>
                `;
            }
        } catch (error) {
            console.error('Error executing code:', error);
            outputElement.innerHTML = `
                <div class="output-error">
                    <strong class="text-danger">Connection Error:</strong>
                    <p class="mt-2 mb-0 text-danger">Unable to connect to code execution service. Please check your internet connection or try again later.</p>
                    <details class="mt-2">
                        <summary class="small">Debug Info</summary>
                        <pre class="small mt-1">${this.escapeHtml(error.toString())}</pre>
                    </details>
                </div>
            `;
        }
    }

    async callJDoodleAPI(code) {
        // Note: You need to sign up at JDoodle.com for free API credentials
        // Replace these with your actual credentials
        const clientId = 'YOUR_JD00DLE_CLIENT_ID';
        const clientSecret = 'YOUR_JD00DLE_CLIENT_SECRET';
        
        // For demo purposes, we'll simulate API response
        // Remove this simulation when you have real credentials
        return await this.simulateCodeExecution(code);
        
        // Uncomment below when you have JDoodle credentials
        /*
        const response = await fetch('https://api.jdoodle.com/v1/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                clientId: clientId,
                clientSecret: clientSecret,
                script: code,
                language: 'c',
                versionIndex: '0'
            })
        });
        
        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        
        return await response.json();
        */
    }

    // Simulation for demo purposes
    async simulateCodeExecution(code) {
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // Simple code analysis for simulation
        if (code.includes('printf') && code.includes('Hello')) {
            return {
                output: 'Hello, World!\n',
                statusCode: 200,
                memory: '1234',
                cpuTime: '0.00'
            };
        } else if (code.includes('error') || code.includes('Error')) {
            return {
                error: 'simulated_error: This is a simulated compilation error\nundefined reference to `simulated_error\'\n',
                statusCode: 200
            };
        } else {
            return {
                output: 'Code executed successfully!\nOutput would appear here with real API credentials.',
                statusCode: 200,
                memory: '1234',
                cpuTime: '0.00'
            };
        }
    }

    escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
}

// Initialize code editor when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on a page with code blocks
    const codeBlocks = document.querySelectorAll('pre code.language-c');
    if (codeBlocks.length > 0) {
        window.codeEditor = new CodeEditor();
    }
});

// Additional code formatting utilities
function formatCode(textarea) {
    const code = textarea.value;
    // Simple indentation helper
    const formatted = code.replace(/\t/g, '    '); // Convert tabs to 4 spaces
    textarea.value = formatted;
}

// Copy to clipboard functionality
function setupCopyButtons() {
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('copy-code-btn')) {
            const button = e.target;
            const codeContainer = button.closest('.code-editor-container');
            const textarea = codeContainer.querySelector('.code-textarea');
            
            navigator.clipboard.writeText(textarea.value).then(function() {
                const originalText = button.innerHTML;
                button.innerHTML = '<i class="fas fa-check me-1"></i> Copied!';
                button.classList.add('btn-success');
                
                setTimeout(function() {
                    button.innerHTML = originalText;
                    button.classList.remove('btn-success');
                }, 2000);
            }).catch(function(err) {
                console.error('Failed to copy code: ', err);
                alert('Failed to copy code to clipboard');
            });
        }
    });
}

// Initialize copy buttons when DOM is loaded
document.addEventListener('DOMContentLoaded', setupCopyButtons);