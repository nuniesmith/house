/**
 * Enhanced Markdown Parser Module for Construction Management App
 * Supports construction-specific formatting and styling
 */

class ConstructionMarkdownParser {
    constructor() {
        this.initializeParser();
        this.setupConstructionExtensions();
    }

    initializeParser() {
        // Basic markdown patterns
        this.patterns = {
            // Headers
            h1: /^# (.*$)/gim,
            h2: /^## (.*$)/gim,
            h3: /^### (.*$)/gim,
            h4: /^#### (.*$)/gim,
            h5: /^##### (.*$)/gim,
            h6: /^###### (.*$)/gim,

            // Text formatting
            bold: /\*\*(.*?)\*\*/gim,
            italic: /\*(.*?)\*/gim,
            strikethrough: /~~(.*?)~~/gim,
            code: /`(.*?)`/gim,

            // Lists
            unorderedList: /^\* (.*$)/gim,
            orderedList: /^\d+\. (.*$)/gim,

            // Links and images
            link: /\[([^\]]+)\]\(([^\)]+)\)/gim,
            image: /!\[([^\]]*)\]\(([^\)]+)\)/gim,

            // Code blocks
            codeBlock: /```(\w+)?\n([\s\S]*?)```/gim,

            // Tables
            table: /^\|(.+)\|$/gim,

            // Blockquotes
            blockquote: /^> (.*$)/gim,

            // Horizontal rules
            hr: /^---$/gim,

            // Line breaks
            lineBreak: /\n/gim
        };

        // Construction-specific patterns
        this.constructionPatterns = {
            // Cost patterns
            cost: /\$([0-9,]+(?:\.[0-9]{2})?)/gim,
            costRange: /\$([0-9,]+(?:\.[0-9]{2})?)\s*-\s*\$([0-9,]+(?:\.[0-9]{2})?)/gim,
            
            // Measurement patterns
            measurement: /(\d+(?:\.\d+)?)\s*(sq\s?ft|linear\s?ft|ft|inches?|in|yards?|yd|sq\s?m|m²|meters?|m)/gim,
            
            // Time patterns
            timeframe: /(\d+)\s*(days?|weeks?|months?|years?)/gim,
            
            // Material specifications
            material: /(\d+[×x]\d+|\d+"[×x]\d+"|\d+"\s*×\s*\d+")/gim,
            
            // Code references (building codes, etc.)
            buildingCode: /(R-\d+|ASTM\s+[A-Z]\d+|IRC\s+\d+|IBC\s+\d+|OSHA\s+\d+)/gim,
            
            // Safety notes
            safety: /⚠️|🚨|WARNING|CAUTION|DANGER/gim,
            
            // Phase indicators
            phase: /Phase\s+(\d+)/gim
        };
    }

    setupConstructionExtensions() {
        // Construction-specific CSS classes
        this.constructionStyles = {
            cost: 'construction-cost',
            measurement: 'construction-measurement', 
            timeframe: 'construction-timeframe',
            material: 'construction-material',
            buildingCode: 'construction-code',
            safety: 'construction-safety',
            phase: 'construction-phase'
        };
    }

    parse(markdown) {
        let html = markdown;

        // First pass: Construction-specific formatting
        html = this.parseConstructionElements(html);

        // Second pass: Standard markdown
        html = this.parseStandardMarkdown(html);

        // Third pass: Post-processing
        html = this.postProcess(html);

        return this.wrapInConstructionTheme(html);
    }

    parseConstructionElements(text) {
        let html = text;

        // Parse cost ranges first (before individual costs)
        html = html.replace(this.constructionPatterns.costRange, 
            '<span class="' + this.constructionStyles.cost + ' cost-range">$$$1 - $$$2</span>');

        // Parse individual costs
        html = html.replace(this.constructionPatterns.cost, 
            '<span class="' + this.constructionStyles.cost + '">$$$1</span>');

        // Parse measurements
        html = html.replace(this.constructionPatterns.measurement, 
            '<span class="' + this.constructionStyles.measurement + '">$1 $2</span>');

        // Parse timeframes
        html = html.replace(this.constructionPatterns.timeframe, 
            '<span class="' + this.constructionStyles.timeframe + '">$1 $2</span>');

        // Parse material specifications
        html = html.replace(this.constructionPatterns.material, 
            '<span class="' + this.constructionStyles.material + '">$1</span>');

        // Parse building codes
        html = html.replace(this.constructionPatterns.buildingCode, 
            '<span class="' + this.constructionStyles.buildingCode + '">$1</span>');

        // Parse safety warnings
        html = html.replace(this.constructionPatterns.safety, 
            '<span class="' + this.constructionStyles.safety + '">$&</span>');

        // Parse phases
        html = html.replace(this.constructionPatterns.phase, 
            '<span class="' + this.constructionStyles.phase + '">Phase $1</span>');

        return html;
    }

    parseStandardMarkdown(text) {
        let html = text;

        // Headers (process in reverse order to avoid conflicts)
        html = html.replace(this.patterns.h6, '<h6 class="construction-h6">$1</h6>');
        html = html.replace(this.patterns.h5, '<h5 class="construction-h5">$1</h5>');
        html = html.replace(this.patterns.h4, '<h4 class="construction-h4">$1</h4>');
        html = html.replace(this.patterns.h3, '<h3 class="construction-h3">$1</h3>');
        html = html.replace(this.patterns.h2, '<h2 class="construction-h2">$1</h2>');
        html = html.replace(this.patterns.h1, '<h1 class="construction-h1">$1</h1>');

        // Code blocks (process before inline code)
        html = html.replace(this.patterns.codeBlock, (match, lang, code) => {
            const language = lang || 'text';
            return `<pre class="construction-code-block"><code class="language-${language}">${code.trim()}</code></pre>`;
        });

        // Text formatting
        html = html.replace(this.patterns.bold, '<strong class="construction-bold">$1</strong>');
        html = html.replace(this.patterns.italic, '<em class="construction-italic">$1</em>');
        html = html.replace(this.patterns.strikethrough, '<del class="construction-strikethrough">$1</del>');
        html = html.replace(this.patterns.code, '<code class="construction-inline-code">$1</code>');

        // Links and images
        html = html.replace(this.patterns.image, '<img src="$2" alt="$1" class="construction-image">');
        html = html.replace(this.patterns.link, '<a href="$2" class="construction-link">$1</a>');

        // Blockquotes
        html = html.replace(this.patterns.blockquote, '<blockquote class="construction-blockquote">$1</blockquote>');

        // Horizontal rules
        html = html.replace(this.patterns.hr, '<hr class="construction-hr">');

        return html;
    }

    parseList(text) {
        // Handle unordered lists
        let lines = text.split('\n');
        let inList = false;
        let listType = null;
        let result = [];

        for (let line of lines) {
            if (line.match(/^\* /)) {
                if (!inList || listType !== 'ul') {
                    if (inList) result.push('</ol>');
                    result.push('<ul class="construction-list construction-ul">');
                    inList = true;
                    listType = 'ul';
                }
                result.push('<li class="construction-list-item">' + line.replace(/^\* /, '') + '</li>');
            } else if (line.match(/^\d+\. /)) {
                if (!inList || listType !== 'ol') {
                    if (inList) result.push('</ul>');
                    result.push('<ol class="construction-list construction-ol">');
                    inList = true;
                    listType = 'ol';
                }
                result.push('<li class="construction-list-item">' + line.replace(/^\d+\. /, '') + '</li>');
            } else {
                if (inList) {
                    result.push(listType === 'ul' ? '</ul>' : '</ol>');
                    inList = false;
                    listType = null;
                }
                result.push(line);
            }
        }

        if (inList) {
            result.push(listType === 'ul' ? '</ul>' : '</ol>');
        }

        return result.join('\n');
    }

    parseTable(text) {
        const lines = text.split('\n');
        const tableLines = lines.filter(line => line.trim().startsWith('|'));
        
        if (tableLines.length < 2) return text;

        let tableHtml = '<table class="construction-table">\n';
        
        // Parse header
        const headerCells = tableLines[0].split('|').slice(1, -1).map(cell => cell.trim());
        tableHtml += '<thead class="construction-table-head"><tr class="construction-table-row">';
        headerCells.forEach(cell => {
            tableHtml += `<th class="construction-table-header">${cell}</th>`;
        });
        tableHtml += '</tr></thead>\n';

        // Parse body (skip separator line)
        tableHtml += '<tbody class="construction-table-body">';
        for (let i = 2; i < tableLines.length; i++) {
            const cells = tableLines[i].split('|').slice(1, -1).map(cell => cell.trim());
            tableHtml += '<tr class="construction-table-row">';
            cells.forEach(cell => {
                tableHtml += `<td class="construction-table-cell">${cell}</td>`;
            });
            tableHtml += '</tr>';
        }
        tableHtml += '</tbody></table>';

        return text.replace(tableLines.join('\n'), tableHtml);
    }

    postProcess(html) {
        // Handle lists
        html = this.parseList(html);
        
        // Handle tables
        html = this.parseTable(html);

        // Convert line breaks to <br> tags (but not in code blocks)
        html = html.replace(/\n(?![^<]*<\/(?:pre|code)>)/g, '<br>');

        // Clean up multiple <br> tags
        html = html.replace(/(<br>\s*){3,}/g, '<br><br>');

        return html;
    }

    wrapInConstructionTheme(html) {
        return `
            <div class="construction-document">
                <style>
                    .construction-document {
                        font-family: 'Courier New', monospace;
                        color: #00ff88;
                        background: #1a1a2e;
                        padding: 20px;
                        line-height: 1.6;
                    }
                    
                    .construction-h1, .construction-h2, .construction-h3,
                    .construction-h4, .construction-h5, .construction-h6 {
                        color: #88ff00;
                        margin: 20px 0 10px 0;
                        text-shadow: 0 0 5px currentColor;
                    }
                    
                    .construction-h1 { font-size: 2.5em; border-bottom: 3px solid #88ff00; padding-bottom: 10px; }
                    .construction-h2 { font-size: 2em; border-bottom: 2px solid #88ff00; padding-bottom: 8px; }
                    .construction-h3 { font-size: 1.5em; border-bottom: 1px solid #88ff00; padding-bottom: 5px; }
                    
                    .construction-cost {
                        color: #ffff00;
                        font-weight: bold;
                        background: rgba(255, 255, 0, 0.1);
                        padding: 2px 6px;
                        border-radius: 4px;
                        text-shadow: 0 0 3px #ffff00;
                    }
                    
                    .construction-measurement {
                        color: #ff8800;
                        font-weight: bold;
                        background: rgba(255, 136, 0, 0.1);
                        padding: 2px 6px;
                        border-radius: 4px;
                    }
                    
                    .construction-timeframe {
                        color: #00ffff;
                        font-weight: bold;
                        background: rgba(0, 255, 255, 0.1);
                        padding: 2px 6px;
                        border-radius: 4px;
                    }
                    
                    .construction-material {
                        color: #ff00ff;
                        font-weight: bold;
                        background: rgba(255, 0, 255, 0.1);
                        padding: 2px 6px;
                        border-radius: 4px;
                    }
                    
                    .construction-code {
                        color: #00ff88;
                        font-weight: bold;
                        background: rgba(0, 255, 136, 0.1);
                        padding: 2px 6px;
                        border-radius: 4px;
                        border: 1px solid #00ff88;
                    }
                    
                    .construction-safety {
                        color: #ff4444;
                        font-weight: bold;
                        background: rgba(255, 68, 68, 0.2);
                        padding: 4px 8px;
                        border-radius: 4px;
                        border: 1px solid #ff4444;
                        animation: pulse 2s infinite;
                    }
                    
                    .construction-phase {
                        color: #88ff00;
                        font-weight: bold;
                        background: rgba(136, 255, 0, 0.1);
                        padding: 2px 6px;
                        border-radius: 4px;
                        border: 1px solid #88ff00;
                    }
                    
                    .construction-bold { color: #88ff00; }
                    .construction-italic { color: #ffff00; }
                    .construction-strikethrough { opacity: 0.6; }
                    
                    .construction-inline-code {
                        background: #2a2a5a;
                        color: #00ffff;
                        padding: 2px 6px;
                        border-radius: 4px;
                        font-family: 'Courier New', monospace;
                        border: 1px solid #00ffff;
                    }
                    
                    .construction-code-block {
                        background: #0f0f23;
                        border: 2px solid #00ff88;
                        border-radius: 8px;
                        padding: 15px;
                        margin: 15px 0;
                        overflow-x: auto;
                    }
                    
                    .construction-code-block code {
                        color: #00ffff;
                        font-family: 'Courier New', monospace;
                    }
                    
                    .construction-list {
                        margin: 15px 0;
                        padding-left: 30px;
                    }
                    
                    .construction-list-item {
                        margin: 8px 0;
                        color: #00ff88;
                    }
                    
                    .construction-link {
                        color: #00ffff;
                        text-decoration: underline;
                        transition: color 0.3s ease;
                    }
                    
                    .construction-link:hover {
                        color: #88ff00;
                        text-shadow: 0 0 5px #88ff00;
                    }
                    
                    .construction-image {
                        max-width: 100%;
                        height: auto;
                        border: 2px solid #00ff88;
                        border-radius: 8px;
                        margin: 15px 0;
                    }
                    
                    .construction-blockquote {
                        border-left: 4px solid #88ff00;
                        margin: 15px 0;
                        padding: 10px 20px;
                        background: rgba(136, 255, 0, 0.1);
                        font-style: italic;
                        color: #88ff00;
                    }
                    
                    .construction-hr {
                        border: none;
                        height: 2px;
                        background: linear-gradient(90deg, #00ff88, #88ff00, #00ff88);
                        margin: 30px 0;
                    }
                    
                    .construction-table {
                        width: 100%;
                        border-collapse: collapse;
                        margin: 20px 0;
                        background: #0f0f23;
                        border: 2px solid #00ff88;
                        border-radius: 8px;
                        overflow: hidden;
                    }
                    
                    .construction-table-header {
                        background: #00ff88;
                        color: #0f0f23;
                        padding: 12px;
                        font-weight: bold;
                        text-align: left;
                    }
                    
                    .construction-table-cell {
                        padding: 10px 12px;
                        border-bottom: 1px solid #2a2a5a;
                    }
                    
                    .construction-table-row:hover {
                        background: rgba(0, 255, 136, 0.1);
                    }
                    
                    @keyframes pulse {
                        0%, 100% { opacity: 1; }
                        50% { opacity: 0.7; }
                    }
                </style>
                ${html}
            </div>
        `;
    }

    // Static method for quick parsing
    static parse(markdown) {
        const parser = new ConstructionMarkdownParser();
        return parser.parse(markdown);
    }

    // Method to parse and display in an iframe
    static parseAndDisplay(markdown, targetFrame) {
        const html = ConstructionMarkdownParser.parse(markdown);
        const fullHtml = `
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Construction Guide</title>
            </head>
            <body style="margin: 0; padding: 0;">
                ${html}
            </body>
            </html>
        `;
        
        if (targetFrame) {
            targetFrame.src = 'data:text/html;charset=utf-8,' + encodeURIComponent(fullHtml);
        }
        
        return fullHtml;
    }
}

// Export for module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ConstructionMarkdownParser;
}

// Global availability
window.ConstructionMarkdownParser = ConstructionMarkdownParser;
window.marked = ConstructionMarkdownParser; // Compatibility with marked.js