
(() => {
  const menuButton = document.getElementById('menuToggle');
  const menuPanel = document.getElementById('menuPanel');
  const searchInput = document.getElementById('siteSearch');
  const clearButton = document.getElementById('clearSearch');
  const status = document.getElementById('searchStatus');
  const results = document.getElementById('searchResults');
  const topics = [...document.querySelectorAll('.topic')];
  const themeButton = document.getElementById('themeToggle');
  const printButton = document.getElementById('printGuide');

  const openMenu = (focusSearch = false) => {
    menuPanel.hidden = false;
    menuButton.setAttribute('aria-expanded', 'true');
    if (focusSearch) window.setTimeout(() => searchInput.focus(), 0);
  };
  const closeMenu = () => {
    menuPanel.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
  };
  menuButton.addEventListener('click', () => {
    if (menuPanel.hidden) openMenu(false); else closeMenu();
  });

  document.addEventListener('click', (event) => {
    if (!menuPanel.hidden && !menuPanel.contains(event.target) && !menuButton.contains(event.target)) closeMenu();
  });

  document.addEventListener('keydown', (event) => {
    const target = event.target;
    const typing = target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target.isContentEditable;
    if ((event.key === '/' && !typing) || (event.ctrlKey && event.key.toLowerCase() === 'k')) {
      event.preventDefault();
      openMenu(true);
    }
    if (event.key === 'Escape') {
      if (!menuPanel.hidden) closeMenu();
      else if (searchInput.value) clearSearch();
    }
  });

  const originalTextNodes = new WeakMap();
  const clearMarks = () => {
    document.querySelectorAll('mark[data-search-mark]').forEach(mark => {
      const parent = mark.parentNode;
      parent.replaceChild(document.createTextNode(mark.textContent), mark);
      parent.normalize();
    });
  };

  const highlightTokens = (root, tokens) => {
    if (!tokens.length) return;
    const pattern = new RegExp(`(${tokens.map(t => t.replace(/[.*+?^${}()|[\\]\\]/g, '\\$&')).join('|')})`, 'gi');
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        if (!node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        if (node.parentElement.closest('script, style, code, .formula, .source-links')) return NodeFilter.FILTER_REJECT;
        return pattern.test(node.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(node => {
      pattern.lastIndex = 0;
      const fragment = document.createDocumentFragment();
      let cursor = 0;
      node.nodeValue.replace(pattern, (match, _group, offset) => {
        fragment.appendChild(document.createTextNode(node.nodeValue.slice(cursor, offset)));
        const mark = document.createElement('mark');
        mark.dataset.searchMark = 'true';
        mark.textContent = match;
        fragment.appendChild(mark);
        cursor = offset + match.length;
      });
      fragment.appendChild(document.createTextNode(node.nodeValue.slice(cursor)));
      node.parentNode.replaceChild(fragment, node);
    });
  };

  const search = () => {
    clearMarks();
    const query = searchInput.value.trim().toLowerCase();
    const tokens = [...new Set(query.split(/\s+/).filter(Boolean))];
    results.replaceChildren();
    let matches = 0;

    topics.forEach(topic => {
      const haystack = `${topic.textContent} ${topic.dataset.keywords || ''}`.toLowerCase();
      const isMatch = tokens.length === 0 || tokens.every(token => haystack.includes(token));
      topic.classList.toggle('is-hidden', !isMatch);
      if (isMatch) {
        matches += 1;
        if (tokens.length) highlightTokens(topic, tokens);
        const link = document.createElement('a');
        link.href = `#${topic.id}`;
        link.textContent = topic.querySelector('h2').textContent;
        link.addEventListener('click', closeMenu);
        results.appendChild(link);
      }
    });

    if (!tokens.length) {
      status.textContent = `All ${topics.length} topics shown.`;
      results.replaceChildren();
    } else if (matches) {
      status.textContent = `${matches} topic${matches === 1 ? '' : 's'} match “${searchInput.value.trim()}”.`;
    } else {
      status.textContent = `No topic matches “${searchInput.value.trim()}”. Try a broader term.`;
      const hint = document.createElement('p');
      hint.className = 'search-help';
      hint.textContent = 'Examples: gradient, regularization, CNN, beam, BERT, RAG, MCP, security.';
      results.appendChild(hint);
    }
  };

  const clearSearch = () => {
    searchInput.value = '';
    search();
    searchInput.focus();
  };
  searchInput.addEventListener('input', search);
  clearButton.addEventListener('click', clearSearch);
  document.querySelectorAll('.toc a, .topic-map a').forEach(link => link.addEventListener('click', closeMenu));

  const savedTheme = localStorage.getItem('data785-theme');
  if (savedTheme) document.documentElement.dataset.theme = savedTheme;
  const updateThemeLabel = () => {
    const isDark = document.documentElement.dataset.theme === 'dark';
    themeButton.textContent = isDark ? 'Light' : 'Dark';
    themeButton.setAttribute('aria-label', `Switch to ${isDark ? 'light' : 'dark'} theme`);
  };
  updateThemeLabel();
  themeButton.addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    localStorage.setItem('data785-theme', next);
    updateThemeLabel();
  });
  printButton.addEventListener('click', () => window.print());
  search();
})();
