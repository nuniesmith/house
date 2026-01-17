/**
 * Main Application Controller for Construction Management Suite
 * Handles navigation, state management, and component integration
 */

class ConstructionApp {
    constructor() {
        this.currentProject = 'bunker';
        this.currentView = 'index';
        this.isInitialized = false;
        
        // Project data store
        this.projectData = {
            bunker: {
                name: "Underground Bunker Facility",
                sqft: 15000,
                stories: 6,
                bedrooms: 8,
                bathrooms: 6,
                months: 16,
                progress: 15,
                budget: 28200000,
                cost: 28200000,
                status: "active",
                lastUpdated: new Date().toISOString()
            },
            farmhouse: {
                name: "Modern Farmhouse",
                sqft: 3200,
                stories: 1,
                bedrooms: 4,
                bathrooms: 3,
                months: 8,
                progress: 5,
                budget: 785000,
                cost: 785000,
                status: "planning",
                lastUpdated: new Date().toISOString()
            },
            cabin: {
                name: "Long Creek Cabin",
                sqft: 1577,
                stories: 2,
                bedrooms: 3,
                bathrooms: 2,
                months: 6,
                progress: 85,
                budget: 234000,
                cost: 234000,
                status: "complete",
                lastUpdated: new Date().toISOString()
            }
        };

        // File mappings for navigation
        this.fileMap = {
            'index': 'index.html',
            'calculator': 'calculator.html',
            'dashboard': 'dashboard.html',
            'scheduler': 'scheduler.html',
            'bunker-blueprint': 'bunker.html',
            'bunker-guide': 'bunker.md',
            'farmhouse-blueprint': 'house.html',
            'farmhouse-guide': 'house.md',
            'cabin-blueprint': 'cabin.html',
            'cabin-guide': 'cabin.md'
        };

        this.init();
    }

    init() {
        if (this.isInitialized) return;
        
        console.log('🏗️ Initializing Construction Management App...');
        
        // Load saved state
        this.loadState();
        
        // Setup event listeners
        this.setupEventListeners();
        
        // Setup message handling for iframe communication
        this.setupMessageHandling();
        
        // Initialize navigation
        this.initializeNavigation();
        
        // Setup periodic save
        this.setupPeriodicSave();
        
        this.isInitialized = true;
        console.log('✅ Construction App initialized successfully');
    }

    loadState() {
        try {
            // Load current project
            const savedProject = localStorage.getItem('construction_current_project');
            if (savedProject && this.projectData[savedProject]) {
                this.currentProject = savedProject;
            }

            // Load project data
            const savedData = localStorage.getItem('construction_project_data');
            if (savedData) {
                const parsedData = JSON.parse(savedData);
                this.projectData = { ...this.projectData, ...parsedData };
            }

            // Load current view
            const savedView = localStorage.getItem('construction_current_view');
            if (savedView) {
                this.currentView = savedView;
            }

            console.log('📊 State loaded:', { 
                currentProject: this.currentProject, 
                currentView: this.currentView 
            });
        } catch (error) {
            console.warn('⚠️ Error loading state:', error);
        }
    }

    saveState() {
        try {
            localStorage.setItem('construction_current_project', this.currentProject);
            localStorage.setItem('construction_project_data', JSON.stringify(this.projectData));
            localStorage.setItem('construction_current_view', this.currentView);
            localStorage.setItem('construction_last_save', new Date().toISOString());
        } catch (error) {
            console.warn('⚠️ Error saving state:', error);
        }
    }

    setupEventListeners() {
        // Handle browser navigation
        window.addEventListener('popstate', (event) => {
            if (event.state && event.state.view) {
                this.navigateToView(event.state.view, false);
            }
        });

        // Handle page unload
        window.addEventListener('beforeunload', () => {
            this.saveState();
        });

        // Handle visibility change (save when tab becomes hidden)
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                this.saveState();
            }
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (event) => {
            if (event.ctrlKey || event.metaKey) {
                switch(event.key) {
                    case '1':
                        event.preventDefault();
                        this.navigateToView('index');
                        break;
                    case '2':
                        event.preventDefault();
                        this.navigateToView('calculator');
                        break;
                    case '3':
                        event.preventDefault();
                        this.navigateToView('dashboard');
                        break;
                    case '4':
                        event.preventDefault();
                        this.navigateToView('scheduler');
                        break;
                    case 's':
                        event.preventDefault();
                        this.exportProjectData();
                        break;
                }
            }
        });
    }

    setupMessageHandling() {
        window.addEventListener('message', (event) => {
            // Handle messages from iframe components
            if (event.data && event.data.type) {
                switch (event.data.type) {
                    case 'projectChanged':
                        this.switchProject(event.data.project);
                        break;
                    case 'costUpdated':
                        this.updateProjectCost(event.data.project, event.data.cost);
                        break;
                    case 'progressUpdated':
                        this.updateProjectProgress(event.data.project, event.data.progress);
                        break;
                    case 'navigateToView':
                        this.navigateToView(event.data.view);
                        break;
                    case 'navigateToProject':
                        this.navigateToProject(event.data.project, event.data.view);
                        break;
                    case 'requestProjectData':
                        this.sendProjectDataToFrame(event.data.requestId);
                        break;
                }
            }
        });
    }

    initializeNavigation() {
        // Check URL hash for initial navigation
        const hash = window.location.hash.substring(1);
        if (hash && this.fileMap[hash]) {
            this.navigateToView(hash, false);
        } else if (this.currentView !== 'index') {
            this.navigateToView(this.currentView, false);
        }
    }

    setupPeriodicSave() {
        // Save state every 30 seconds
        setInterval(() => {
            this.saveState();
        }, 30000);
    }

    // Navigation methods
    navigateToView(viewName, updateHistory = true) {
        if (!this.fileMap[viewName]) {
            console.warn(`⚠️ Unknown view: ${viewName}`);
            return;
        }

        console.log(`🧭 Navigating to: ${viewName}`);
        
        this.currentView = viewName;
        
        // Update browser history
        if (updateHistory) {
            const url = `#${viewName}`;
            history.pushState({ view: viewName }, '', url);
        }

        // Handle different view types
        if (viewName.includes('-guide') && viewName.endsWith('.md')) {
            this.loadMarkdownView(viewName);
        } else {
            this.loadHtmlView(viewName);
        }

        // Update UI if on main page
        this.updateNavigationUI(viewName);
        
        this.saveState();
    }

    navigateToProject(projectId, viewType = 'blueprint') {
        const viewName = `${projectId}-${viewType}`;
        this.switchProject(projectId);
        this.navigateToView(viewName);
    }

    loadHtmlView(viewName) {
        const filename = this.fileMap[viewName];
        
        // If we're in a unified app structure, load in iframe
        const iframe = document.getElementById('contentFrame');
        if (iframe) {
            iframe.src = filename;
        } else {
            // If not in unified structure, navigate directly
            window.location.href = filename;
        }
    }

    loadMarkdownView(viewName) {
        const filename = this.fileMap[viewName];
        
        // Load markdown file and convert to HTML
        fetch(filename)
            .then(response => response.text())
            .then(markdown => {
                const iframe = document.getElementById('contentFrame');
                if (iframe && window.ConstructionMarkdownParser) {
                    window.ConstructionMarkdownParser.parseAndDisplay(markdown, iframe);
                } else {
                    // Fallback: create a simple HTML page
                    const html = this.createSimpleMarkdownPage(markdown);
                    iframe.src = 'data:text/html;charset=utf-8,' + encodeURIComponent(html);
                }
            })
            .catch(error => {
                console.error('Error loading markdown:', error);
                this.showError('Failed to load construction guide');
            });
    }

    createSimpleMarkdownPage(markdown) {
        // Simple markdown to HTML conversion for fallback
        let html = markdown
            .replace(/^# (.*$)/gim, '<h1 style="color: #88ff00;">$1</h1>')
            .replace(/^## (.*$)/gim, '<h2 style="color: #88ff00;">$1</h2>')
            .replace(/^### (.*$)/gim, '<h3 style="color: #88ff00;">$1</h3>')
            .replace(/\*\*(.*?)\*\*/gim, '<strong style="color: #88ff00;">$1</strong>')
            .replace(/\*(.*?)\*/gim, '<em style="color: #ffff00;">$1</em>')
            .replace(/^\* (.*$)/gim, '<li>$1</li>')
            .replace(/\n/gim, '<br>');

        return `
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body { 
                        font-family: 'Courier New', monospace; 
                        background: #1a1a2e; 
                        color: #00ff88; 
                        padding: 20px; 
                        line-height: 1.6;
                    }
                    h1, h2, h3 { color: #88ff00; }
                    strong { color: #88ff00; }
                    em { color: #ffff00; }
                    li { margin: 8px 0; }
                </style>
            </head>
            <body>${html}</body>
            </html>
        `;
    }

    updateNavigationUI(viewName) {
        // Update active navigation items
        document.querySelectorAll('.nav-item, .project-link, .tool-link').forEach(item => {
            item.classList.remove('active');
        });

        // Add active class to current view
        const activeItem = document.querySelector(`[data-view="${viewName}"]`);
        if (activeItem) {
            activeItem.classList.add('active');
        }

        // Update breadcrumb if exists
        const breadcrumb = document.getElementById('breadcrumb');
        if (breadcrumb) {
            breadcrumb.textContent = this.getViewTitle(viewName);
        }
    }

    getViewTitle(viewName) {
        const titles = {
            'index': '🏗️ Construction Projects HQ',
            'calculator': '🧮 Universal Cost Calculator',
            'dashboard': '📊 Project Dashboard',
            'scheduler': '📅 Project Scheduler',
            'bunker-blueprint': '🏢 Bunker Blueprints',
            'bunker-guide': '📋 Bunker Construction Guide',
            'farmhouse-blueprint': '🏡 Farmhouse Blueprints',
            'farmhouse-guide': '📋 Farmhouse Construction Guide',
            'cabin-blueprint': '🏘️ Cabin Blueprints',
            'cabin-guide': '📋 Cabin Construction Guide'
        };
        return titles[viewName] || '🏗️ Construction Management';
    }

    // Project management methods
    switchProject(projectId) {
        if (!this.projectData[projectId]) {
            console.warn(`⚠️ Unknown project: ${projectId}`);
            return;
        }

        console.log(`🔄 Switching to project: ${projectId}`);
        this.currentProject = projectId;
        
        // Broadcast project change to all iframes
        this.broadcastMessage({
            type: 'projectChanged',
            project: projectId,
            data: this.projectData[projectId]
        });

        this.saveState();
    }

    updateProjectCost(projectId, newCost) {
        if (this.projectData[projectId]) {
            this.projectData[projectId].cost = newCost;
            this.projectData[projectId].budget = newCost;
            this.projectData[projectId].lastUpdated = new Date().toISOString();
            
            console.log(`💰 Updated ${projectId} cost: $${newCost.toLocaleString()}`);
            this.saveState();
            
            // Notify other components
            this.broadcastMessage({
                type: 'costUpdated',
                project: projectId,
                cost: newCost
            });
        }
    }

    updateProjectProgress(projectId, newProgress) {
        if (this.projectData[projectId]) {
            this.projectData[projectId].progress = newProgress;
            this.projectData[projectId].lastUpdated = new Date().toISOString();
            
            console.log(`📈 Updated ${projectId} progress: ${newProgress}%`);
            this.saveState();
            
            // Notify other components
            this.broadcastMessage({
                type: 'progressUpdated',
                project: projectId,
                progress: newProgress
            });
        }
    }

    broadcastMessage(message) {
        // Send message to all iframes
        const iframes = document.querySelectorAll('iframe');
        iframes.forEach(iframe => {
            if (iframe.contentWindow) {
                iframe.contentWindow.postMessage(message, '*');
            }
        });
    }

    sendProjectDataToFrame(requestId) {
        // Send current project data to requesting frame
        this.broadcastMessage({
            type: 'projectDataResponse',
            requestId: requestId,
            currentProject: this.currentProject,
            projectData: this.projectData[this.currentProject],
            allProjects: this.projectData
        });
    }

    // Utility methods
    exportProjectData() {
        const dataStr = JSON.stringify(this.projectData, null, 2);
        const dataBlob = new Blob([dataStr], { type: 'application/json' });
        const url = URL.createObjectURL(dataBlob);
        
        const link = document.createElement('a');
        link.href = url;
        link.download = `construction_projects_${new Date().toISOString().split('T')[0]}.json`;
        link.click();
        
        URL.revokeObjectURL(url);
        console.log('📤 Project data exported');
    }

    importProjectData(file) {
        const reader = new FileReader();
        reader.onload = (event) => {
            try {
                const importedData = JSON.parse(event.target.result);
                
                // Validate data structure
                if (this.validateProjectData(importedData)) {
                    this.projectData = { ...this.projectData, ...importedData };
                    this.saveState();
                    console.log('📥 Project data imported successfully');
                    alert('Project data imported successfully!');
                } else {
                    throw new Error('Invalid data format');
                }
            } catch (error) {
                console.error('❌ Import failed:', error);
                alert('Failed to import project data. Please check the file format.');
            }
        };
        reader.readAsText(file);
    }

    validateProjectData(data) {
        // Basic validation of project data structure
        if (typeof data !== 'object') return false;
        
        for (const [key, project] of Object.entries(data)) {
            if (!project.name || typeof project.cost !== 'number') {
                return false;
            }
        }
        
        return true;
    }

    showError(message) {
        console.error('❌', message);
        // You could enhance this with a proper notification system
        alert(message);
    }

    // Public API methods for external use
    getCurrentProject() {
        return this.projectData[this.currentProject];
    }

    getAllProjects() {
        return this.projectData;
    }

    getProjectStats() {
        const projects = Object.values(this.projectData);
        return {
            totalProjects: projects.length,
            totalValue: projects.reduce((sum, p) => sum + p.cost, 0),
            totalSqFt: projects.reduce((sum, p) => sum + p.sqft, 0),
            totalMonths: projects.reduce((sum, p) => sum + p.months, 0),
            averageProgress: projects.reduce((sum, p) => sum + p.progress, 0) / projects.length
        };
    }
}

// Global utility functions for backward compatibility
function openBlueprint(project) {
    if (window.constructionApp) {
        window.constructionApp.navigateToProject(project, 'blueprint');
    } else {
        window.open(`${project}.html`, '_blank');
    }
}

function openGuide(project) {
    if (window.constructionApp) {
        window.constructionApp.navigateToProject(project, 'guide');
    } else {
        alert(`Opening ${project} construction guide...`);
    }
}

function openCalculator(project = null) {
    if (window.constructionApp) {
        if (project) {
            window.constructionApp.switchProject(project);
        }
        window.constructionApp.navigateToView('calculator');
    } else {
        window.open('calculator.html', '_blank');
    }
}

function openDashboard() {
    if (window.constructionApp) {
        window.constructionApp.navigateToView('dashboard');
    } else {
        window.open('dashboard.html', '_blank');
    }
}

function openScheduler() {
    if (window.constructionApp) {
        window.constructionApp.navigateToView('scheduler');
    } else {
        window.open('scheduler.html', '_blank');
    }
}

// Initialize the app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.constructionApp = new ConstructionApp();
    
    // Make app globally available for debugging
    if (typeof window !== 'undefined') {
        window.ConstructionApp = ConstructionApp;
    }
    
    console.log('🏗️ Construction Management App ready!');
});

// Export for module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ConstructionApp;
}