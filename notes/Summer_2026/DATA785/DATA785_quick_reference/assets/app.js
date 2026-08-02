(() => {
  const menuButton = document.getElementById('menuToggle');
  const menuPanel = document.getElementById('menuPanel');
  const searchInput = document.getElementById('siteSearch');
  const clearButton = document.getElementById('clearSearch');
  const status = document.getElementById('searchStatus');
  const results = document.getElementById('searchResults');
  const searchHelp = document.getElementById('searchHelp');
  const topics = [...document.querySelectorAll('.topic')];
  const themeButton = document.getElementById('themeToggle');
  const printButton = document.getElementById('printGuide');

  const resultTypes = [
    ['all', 'All'],
    ['definition', 'Definitions'],
    ['equation', 'Equations'],
    ['procedure', 'Procedures'],
    ['comparison', 'Comparisons'],
    ['failure', 'Failures'],
    ['example', 'Examples'],
    ['gap-fill', 'Gap fills']
  ];

  const synonymGroups = [
    ['mcp', 'model context protocol'],
    ['mcp structure', 'mcp architecture', 'mcp anatomy', 'host client server'],
    ['agentic tool', 'agent tool', 'tool use', 'function calling', 'function call', 'tool call', 'capability'],
    ['cot', 'chain of thought'],
    ['react', 'reasoning and acting'],
    ['rag', 'retrieval augmented generation'],
    ['rlhf', 'reinforcement learning from human feedback'],
    ['mlp', 'multilayer perceptron', 'multi layer perceptron', 'feedforward neural network', 'feed forward neural network'],
    ['cnn', 'convolutional neural network'],
    ['rnn', 'recurrent neural network'],
    ['lstm', 'long short term memory'],
    ['gru', 'gated recurrent unit'],
    ['bptt', 'backpropagation through time'],
    ['backprop', 'back propagation', 'backpropagation'],
    ['cross entropy', 'cross-entropy'],
    ['binary cross entropy', 'bce'],
    ['mean squared error', 'mse'],
    ['stochastic gradient descent', 'sgd'],
    ['batch normalization', 'batch norm'],
    ['layer normalization', 'layer norm'],
    ['multihead attention', 'multi head attention', 'multi-head attention'],
    ['word2vec', 'word embedding', 'word embeddings'],
    ['beam', 'beam search'],
    ['top p', 'top-p', 'nucleus sampling'],
    ['normalizing flow', 'normalizing flows', 'nf'],
    ['diffusion', 'denoising diffusion probabilistic model', 'ddpm'],
    ['failure mode', 'risk', 'limitation', 'weakness'],
    ['gradient descent', 'optimizer', 'optimization'],
    ['self attention', 'self-attention'],
    ['residual connection', 'skip connection'],
    ['retrieval', 'search', 'lookup']
  ];

  const relatedConcepts = {
    mcp: ['agentic tool', 'function calling', 'permissions', 'host client server'],
    'agentic tool': ['MCP', 'ReAct', 'least privilege', 'function calling'],
    agent: ['ReAct', 'workflow', 'tool use', 'evaluation'],
    backpropagation: ['chain rule', 'autograd', 'vanishing gradients', 'gradient descent'],
    transformer: ['self-attention', 'causal masking', 'residual connections', 'layer normalization'],
    rag: ['embeddings', 'retrieval', 'groundedness', 'prompt injection'],
    rnn: ['BPTT', 'LSTM', 'GRU', 'teacher forcing'],
    diffusion: ['forward process', 'reverse process', 'noise prediction', 'ELBO'],
    cnn: ['convolution', 'pooling', 'padding', 'translation invariance']
  };

  const sourcePrefixes = new Set(['external', 'course', 'current']);
  const typePrefixes = new Map([
    ['definition', 'definition'],
    ['equation', 'equation'],
    ['formula', 'equation'],
    ['procedure', 'procedure'],
    ['process', 'procedure'],
    ['comparison', 'comparison'],
    ['compare', 'comparison'],
    ['failure', 'failure'],
    ['risk', 'failure'],
    ['example', 'example'],
    ['gap', 'gap-fill'],
    ['source', 'source']
  ]);

  const normalize = value => value
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[‐‑‒–—―−]/g, '-')
    .replace(/&/g, ' and ')
    .replace(/[_/\\-]+/g, ' ')
    .replace(/[^a-zA-Z0-9+.#\s]/g, ' ')
    .toLowerCase()
    .replace(/\s+/g, ' ')
    .trim();

  const slugify = value => normalize(value)
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 72) || 'section';

  const aliasLookup = new Map();
  synonymGroups.forEach(group => {
    const normalizedGroup = [...new Set(group.map(normalize))];
    normalizedGroup.forEach(term => aliasLookup.set(term, normalizedGroup));
  });

  const variantsFor = term => {
    const normalizedTerm = normalize(term);
    const direct = aliasLookup.get(normalizedTerm) || [normalizedTerm];
    const variants = new Set(direct);
    direct.forEach(item => {
      if (item.endsWith('ies') && item.length > 4) variants.add(`${item.slice(0, -3)}y`);
      if (item.endsWith('es') && item.length > 4) variants.add(item.slice(0, -2));
      if (item.endsWith('s') && item.length > 3) variants.add(item.slice(0, -1));
      else if (item.length > 3) variants.add(`${item}s`);
    });
    return [...variants].filter(Boolean);
  };

  const uniqueId = (() => {
    const used = new Set([...document.querySelectorAll('[id]')].map(element => element.id));
    return base => {
      let id = base;
      let suffix = 2;
      while (used.has(id)) id = `${base}-${suffix++}`;
      used.add(id);
      return id;
    };
  })();


  const replaceUrl = value => {
    try {
      history.replaceState(null, '', value);
    } catch (_error) {
      if (typeof value === 'string' && value.includes('#')) {
        const hash = value.slice(value.indexOf('#'));
        try { window.location.hash = hash; } catch (_ignored) { /* URL state is optional. */ }
      }
    }
  };

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
    if (menuPanel.hidden) openMenu(false);
    else closeMenu();
  });

  document.addEventListener('click', event => {
    if (!menuPanel.hidden && !menuPanel.contains(event.target) && !menuButton.contains(event.target)) closeMenu();
  });

  const searchSection = searchInput.closest('section');
  const searchTools = document.createElement('div');
  searchTools.className = 'search-tools';

  const scopeLabel = document.createElement('label');
  scopeLabel.className = 'search-scope';
  scopeLabel.innerHTML = '<span>Scope</span>';
  const scopeSelect = document.createElement('select');
  scopeSelect.id = 'searchScope';
  scopeSelect.setAttribute('aria-label', 'Search scope');
  scopeSelect.append(new Option('All topics', 'all'));
  topics.forEach(topic => {
    const title = topic.querySelector('h2')?.textContent.trim() || topic.id;
    scopeSelect.append(new Option(title, topic.id));
  });
  scopeLabel.appendChild(scopeSelect);
  searchTools.appendChild(scopeLabel);

  const filterGroup = document.createElement('div');
  filterGroup.className = 'search-filters';
  filterGroup.setAttribute('role', 'group');
  filterGroup.setAttribute('aria-label', 'Search result type');
  resultTypes.forEach(([value, label]) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'search-filter';
    button.dataset.filter = value;
    button.textContent = label;
    button.setAttribute('aria-pressed', value === 'all' ? 'true' : 'false');
    filterGroup.appendChild(button);
  });
  searchTools.appendChild(filterGroup);
  searchHelp.after(searchTools);
  searchHelp.innerHTML = 'Use <kbd>/</kbd> or <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>K</kbd>. Try quotes, <code>OR</code>, exclusions such as <code>-security</code>, or prefixes such as <code>definition:MCP</code>.';

  const relatedPanel = document.createElement('div');
  relatedPanel.className = 'search-related';
  relatedPanel.hidden = true;
  results.after(relatedPanel);

  let selectedType = 'all';
  let renderedLimit = 30;
  let currentResultIndex = -1;
  let latestMatches = [];
  let initializing = true;

  const setSelectedType = value => {
    selectedType = resultTypes.some(([type]) => type === value) ? value : 'all';
    filterGroup.querySelectorAll('.search-filter').forEach(button => {
      button.setAttribute('aria-pressed', button.dataset.filter === selectedType ? 'true' : 'false');
    });
  };

  const nearestHeading = (element, topic) => {
    const headings = [...topic.querySelectorAll('h3, h4')];
    let nearest = null;
    headings.forEach(heading => {
      if (heading.compareDocumentPosition(element) & Node.DOCUMENT_POSITION_FOLLOWING) nearest = heading;
    });
    return nearest;
  };

  const classifyText = text => {
    const value = normalize(text);
    const types = new Set();
    if (/definition|terminology|anatomy|structure|component|core role|what is|meaning/.test(value)) types.add('definition');
    if (/equation|formula|objective|loss function|gradient|probability statement/.test(value)) types.add('equation');
    if (/procedure|process|pipeline|workflow|loop|steps|stage|training cycle|interaction|protocol flow|how to/.test(value)) types.add('procedure');
    if (/comparison|compare|versus| vs |difference|trade off|tradeoff|pros|cons/.test(` ${value} `)) types.add('comparison');
    if (/failure|risk|threat|limitation|weakness|caution|security|attack|error|gap/.test(value)) types.add('failure');
    if (/example|scenario|illustration|worked/.test(value)) types.add('example');
    if (/external gap fill|gap fill|alternative source|course note gap|provenance/.test(value)) types.add('gap-fill');
    return types;
  };

  const sourceTypeFor = element => {
    if (element.closest('.provenance-external, .external') || /external gap fill|alternative source/i.test(element.textContent)) return 'external';
    if (element.closest('.provenance-current') || /current-spec|current specification/i.test(element.textContent)) return 'current';
    return 'course';
  };

  const elementText = element => {
    if (!element) return '';
    return (element.innerText || element.textContent || '').replace(/\s+/g, ' ').trim();
  };

  const shortText = (value, max = 120) => {
    const compact = value.replace(/\s+/g, ' ').trim();
    return compact.length > max ? `${compact.slice(0, max - 1).trim()}…` : compact;
  };

  const recordKeySet = new Set();
  const searchRecords = [];
  const addRecord = record => {
    const text = record.body.replace(/\s+/g, ' ').trim();
    if (!text || text.length < 3) return;
    const key = `${record.targetId}|${normalize(record.title)}|${record.types.sort().join(',')}`;
    if (recordKeySet.has(key)) return;
    recordKeySet.add(key);
    const topic = document.getElementById(record.topicId);
    const keywords = topic?.dataset.keywords || '';
    searchRecords.push({
      ...record,
      body: text,
      titleNorm: normalize(record.title),
      headingNorm: normalize(record.headingTitle || ''),
      topicTitleNorm: normalize(record.topicTitle),
      bodyNorm: normalize(text),
      keywordNorm: normalize(keywords),
      sourceType: record.sourceType || 'course'
    });
  };

  topics.forEach(topic => {
    const topicHeading = topic.querySelector('h2');
    const topicTitle = topicHeading?.textContent.trim() || topic.id;
    if (topicHeading && !topicHeading.id) topicHeading.id = uniqueId(`${topic.id}-overview`);

    topic.querySelectorAll('h3, h4').forEach(heading => {
      if (!heading.id) heading.id = uniqueId(`${topic.id}-${slugify(heading.textContent)}`);
      let body = '';
      let sibling = heading.nextElementSibling;
      while (sibling && !/^H[234]$/.test(sibling.tagName)) {
        body += ` ${elementText(sibling)}`;
        sibling = sibling.nextElementSibling;
      }
      if (!body.trim()) body = elementText(heading.parentElement) || heading.textContent;
      const types = classifyText(`${heading.textContent} ${body}`);
      addRecord({
        topicId: topic.id,
        topicTitle,
        headingTitle: heading.textContent.trim(),
        title: heading.textContent.trim(),
        body,
        targetId: heading.id,
        types: [...types],
        sourceType: sourceTypeFor(heading),
        level: Number(heading.tagName.slice(1)),
        weight: heading.tagName === 'H3' ? 30 : 25
      });
    });

    const semanticBlocks = topic.querySelectorAll('.definition, .formula, .callout, details, .card, .architecture > div, .flow, table tbody tr');
    semanticBlocks.forEach(block => {
      if (block.closest('.source-links')) return;
      if (!block.id) block.id = uniqueId(`${topic.id}-${slugify(shortText(elementText(block), 54))}`);
      const heading = nearestHeading(block, topic);
      const headingTitle = heading?.textContent.trim() || topicTitle;
      const text = elementText(block);
      const types = classifyText(`${headingTitle} ${text}`);
      let title = headingTitle;
      let weight = 12;
      let preferredType = null;

      if (block.classList.contains('definition')) {
        types.add('definition');
        preferredType = 'definition';
        title = shortText(text.replace(/^Structural definition\.\s*/i, ''), 92) || headingTitle;
        weight = 35;
      } else if (block.classList.contains('formula')) {
        types.add('equation');
        preferredType = 'equation';
        title = `Equation · ${headingTitle}`;
        weight = 32;
      } else if (block.matches('table tbody tr')) {
        const cells = [...block.querySelectorAll('th, td')];
        title = shortText(cells[0]?.textContent || headingTitle, 86);
        const tableText = normalize(block.closest('table')?.textContent || '');
        if (/term meaning|term definition|role responsibility|component purpose/.test(tableText)) { types.add('definition'); preferredType = 'definition'; }
        if (/comparison|difference|versus|workflow agent|method/.test(tableText)) { types.add('comparison'); preferredType = preferredType || 'comparison'; }
        weight = 17;
      } else if (block.matches('details')) {
        title = block.querySelector('summary')?.textContent.trim() || headingTitle;
        weight = 24;
      } else if (block.matches('.architecture > div')) {
        types.add('procedure');
        preferredType = 'procedure';
        title = block.querySelector('strong')?.textContent.trim() || headingTitle;
        weight = 22;
      } else if (block.classList.contains('flow')) {
        types.add('procedure');
        preferredType = 'procedure';
        title = `${headingTitle} · flow`;
        weight = 22;
      } else if (block.classList.contains('callout')) {
        const strong = block.querySelector('strong')?.textContent.trim();
        title = strong || headingTitle;
        weight = 24;
      } else if (block.classList.contains('card')) {
        title = block.querySelector('h3, h4, strong')?.textContent.trim() || headingTitle;
        weight = 18;
      }

      const sourceType = sourceTypeFor(block);
      if (sourceType === 'external') { types.add('gap-fill'); preferredType = preferredType || 'gap-fill'; }
      addRecord({
        topicId: topic.id,
        topicTitle,
        headingTitle,
        title,
        body: text,
        targetId: block.id,
        types: [...types],
        sourceType,
        preferredType,
        level: 5,
        weight
      });
    });

    addRecord({
      topicId: topic.id,
      topicTitle,
      headingTitle: topicTitle,
      title: topicTitle,
      body: elementText(topic),
      targetId: topic.id,
      types: [],
      sourceType: 'course',
      level: 2,
      weight: 5
    });
  });

  const parseGroup = groupText => {
    const required = [];
    const excluded = [];
    const types = new Set();
    const sources = new Set();
    const tokens = groupText.match(/"[^"]+"|\S+/g) || [];

    tokens.forEach(rawToken => {
      let token = rawToken;
      let excludedToken = false;
      if (token.startsWith('-') && token.length > 1) {
        excludedToken = true;
        token = token.slice(1);
      }
      const quoted = token.startsWith('"') && token.endsWith('"');
      if (quoted) token = token.slice(1, -1);

      const prefixMatch = token.match(/^([a-z-]+):(.*)$/i);
      if (prefixMatch && typePrefixes.has(prefixMatch[1].toLowerCase())) {
        const prefix = typePrefixes.get(prefixMatch[1].toLowerCase());
        const remainder = prefixMatch[2];
        if (prefix === 'source') {
          const sourceValue = normalize(remainder);
          if (sourcePrefixes.has(sourceValue)) sources.add(sourceValue);
        } else {
          types.add(prefix);
          if (remainder) required.push({ value: remainder, quoted: false, variants: variantsFor(remainder) });
        }
        return;
      }

      const term = { value: token, quoted, variants: quoted ? [normalize(token)] : variantsFor(token) };
      if (excludedToken) excluded.push(term);
      else required.push(term);
    });

    return { required, excluded, types, sources };
  };

  const parseQuery = rawQuery => {
    const trimmed = rawQuery.trim();
    const groups = trimmed ? trimmed.split(/\s+OR\s+/i).map(parseGroup) : [parseGroup('')];
    return { raw: trimmed, normalized: normalize(trimmed), groups };
  };

  const containsVariant = (record, variants) => variants.some(variant => {
    if (!variant) return false;
    return record.titleNorm.includes(variant)
      || record.headingNorm.includes(variant)
      || record.topicTitleNorm.includes(variant)
      || record.bodyNorm.includes(variant)
      || record.keywordNorm.includes(variant);
  });

  const matchesType = (record, types) => !types.size || [...types].every(type => record.types.includes(type));
  const matchesSource = (record, sources) => !sources.size || sources.has(record.sourceType);

  const groupMatches = (record, group) => {
    if (!matchesType(record, group.types) || !matchesSource(record, group.sources)) return false;
    if (group.excluded.some(term => containsVariant(record, term.variants))) return false;
    return group.required.every(term => containsVariant(record, term.variants));
  };

  const scoreRecord = (record, parsed) => {
    let score = record.weight;
    const fullQuery = parsed.normalized.replace(/\bor\b/g, ' ').replace(/\s+/g, ' ').trim();
    if (fullQuery) {
      if (record.titleNorm === fullQuery) score += 220;
      else if (record.titleNorm.startsWith(fullQuery)) score += 145;
      else if (record.titleNorm.includes(fullQuery)) score += 100;
      if (record.headingNorm.includes(fullQuery)) score += 80;
      if (record.bodyNorm.includes(fullQuery)) score += 35;
    }

    parsed.groups.forEach(group => {
      group.required.forEach(term => {
        let best = 0;
        term.variants.forEach(variant => {
          if (record.titleNorm === variant) best = Math.max(best, 180);
          else if (record.titleNorm.startsWith(variant)) best = Math.max(best, 115);
          else if (record.titleNorm.includes(variant)) best = Math.max(best, 80);
          if (record.headingNorm.includes(variant)) best = Math.max(best, 68);
          if (record.topicTitleNorm.includes(variant)) best = Math.max(best, 48);
          if (record.bodyNorm.includes(variant)) best = Math.max(best, term.quoted ? 34 : 18);
          if (record.keywordNorm.includes(variant)) best = Math.max(best, 10);
        });
        score += best;
      });
    });

    if (selectedType !== 'all' && record.types.includes(selectedType)) score += 28;
    if (record.sourceType === 'external') score -= 2;
    if (record.level === 2) score -= 15;
    return score;
  };

  const compactMatches = records => {
    const selected = [];
    const perHeading = new Map();
    const perTopic = new Map();
    const topicsWithSpecificMatches = new Set(records.filter(record => record.level > 2).map(record => record.topicId));

    records.forEach(record => {
      if (record.level === 2 && topicsWithSpecificMatches.has(record.topicId)) return;
      const headingKey = `${record.topicId}|${record.headingNorm}|${record.preferredType || record.types.join(',')}`;
      if ((perHeading.get(headingKey) || 0) >= 5) return;
      if ((perTopic.get(record.topicId) || 0) >= 24) return;

      const duplicate = selected.some(existing => {
        if (existing.topicId !== record.topicId || existing.headingNorm !== record.headingNorm) return false;
        if (existing.titleNorm === record.titleNorm) return true;
        const shorter = existing.bodyNorm.length <= record.bodyNorm.length ? existing.bodyNorm : record.bodyNorm;
        const longer = existing.bodyNorm.length > record.bodyNorm.length ? existing.bodyNorm : record.bodyNorm;
        return shorter.length > 90 && longer.includes(shorter);
      });
      if (duplicate) return;

      selected.push(record);
      perHeading.set(headingKey, (perHeading.get(headingKey) || 0) + 1);
      perTopic.set(record.topicId, (perTopic.get(record.topicId) || 0) + 1);
    });
    return selected;
  };

  const visiblePositiveTerms = parsed => {
    const values = [];
    parsed.groups.forEach(group => group.required.forEach(term => values.push(term.value)));
    return [...new Set(values.map(value => value.trim()).filter(Boolean))];
  };

  const escapeRegExp = value => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

  const clearMarks = () => {
    document.querySelectorAll('mark[data-search-mark]').forEach(mark => {
      const parent = mark.parentNode;
      if (!parent) return;
      parent.replaceChild(document.createTextNode(mark.textContent), mark);
      parent.normalize();
    });
  };

  const highlightTokens = (root, tokens) => {
    if (!tokens.length) return;
    const usable = [...new Set(tokens.map(token => token.trim()).filter(Boolean))]
      .sort((a, b) => b.length - a.length);
    if (!usable.length) return;
    const pattern = new RegExp(`(${usable.map(escapeRegExp).join('|')})`, 'gi');
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        if (!node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        if (node.parentElement.closest('script, style, code, .source-links, .menu-panel')) return NodeFilter.FILTER_REJECT;
        pattern.lastIndex = 0;
        return pattern.test(node.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(node => {
      pattern.lastIndex = 0;
      const source = node.nodeValue;
      const fragment = document.createDocumentFragment();
      let cursor = 0;
      source.replace(pattern, (match, _group, offset) => {
        fragment.appendChild(document.createTextNode(source.slice(cursor, offset)));
        const mark = document.createElement('mark');
        mark.dataset.searchMark = 'true';
        mark.textContent = match;
        fragment.appendChild(mark);
        cursor = offset + match.length;
        return match;
      });
      fragment.appendChild(document.createTextNode(source.slice(cursor)));
      node.parentNode.replaceChild(fragment, node);
    });
  };

  const appendHighlightedText = (element, text, terms) => {
    const usable = [...new Set(terms.flatMap(variantsFor).filter(Boolean))]
      .sort((a, b) => b.length - a.length)
      .slice(0, 20);
    if (!usable.length) {
      element.textContent = text;
      return;
    }
    const pattern = new RegExp(`(${usable.map(escapeRegExp).join('|')})`, 'gi');
    let cursor = 0;
    text.replace(pattern, (match, _group, offset) => {
      element.appendChild(document.createTextNode(text.slice(cursor, offset)));
      const mark = document.createElement('mark');
      mark.textContent = match;
      element.appendChild(mark);
      cursor = offset + match.length;
      return match;
    });
    element.appendChild(document.createTextNode(text.slice(cursor)));
  };

  const makeSnippet = (record, terms, maxLength = 210) => {
    const text = record.body.replace(/\s+/g, ' ').trim();
    if (text.length <= maxLength) return text;
    const lower = text.toLowerCase();
    let index = -1;
    terms.flatMap(variantsFor).some(term => {
      const found = lower.indexOf(term.toLowerCase());
      if (found >= 0) {
        index = found;
        return true;
      }
      return false;
    });
    if (index < 0) index = 0;
    const start = Math.max(0, index - 72);
    const end = Math.min(text.length, start + maxLength);
    return `${start > 0 ? '…' : ''}${text.slice(start, end).trim()}${end < text.length ? '…' : ''}`;
  };

  const primaryType = record => {
    if (selectedType !== 'all' && record.types.includes(selectedType)) return selectedType;
    if (record.preferredType) return record.preferredType;
    const order = ['definition', 'equation', 'procedure', 'comparison', 'failure', 'example', 'gap-fill'];
    return order.find(type => record.types.includes(type)) || 'reference';
  };

  const openTarget = (record, keepOpen = false) => {
    const target = document.getElementById(record.targetId);
    if (!target) return;
    let parent = target.parentElement;
    while (parent) {
      if (parent.tagName === 'DETAILS') parent.open = true;
      parent = parent.parentElement;
    }
    document.querySelectorAll('.search-current').forEach(element => element.classList.remove('search-current'));
    target.classList.add('search-current');
    target.setAttribute('tabindex', '-1');
    if (!keepOpen) closeMenu();
    window.setTimeout(() => {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      target.focus({ preventScroll: true });
    }, 0);
  };

  const renderResult = (record, parsed, index) => {
    const link = document.createElement('a');
    link.className = 'search-result';
    link.href = `#${record.targetId}`;
    link.dataset.resultIndex = String(index);

    const top = document.createElement('span');
    top.className = 'search-result-top';
    const title = document.createElement('strong');
    title.className = 'search-result-title';
    appendHighlightedText(title, record.title, visiblePositiveTerms(parsed));
    const badge = document.createElement('span');
    const type = primaryType(record);
    badge.className = `result-type result-type-${type}`;
    badge.textContent = type.replace('-', ' ');
    top.append(title, badge);

    const meta = document.createElement('span');
    meta.className = 'search-result-meta';
    const breadcrumb = record.headingTitle && normalize(record.headingTitle) !== normalize(record.title)
      ? `${record.topicTitle} → ${record.headingTitle}`
      : record.topicTitle;
    meta.textContent = breadcrumb;

    const snippet = document.createElement('span');
    snippet.className = 'search-result-snippet';
    appendHighlightedText(snippet, makeSnippet(record, visiblePositiveTerms(parsed)), visiblePositiveTerms(parsed));

    link.append(top, meta, snippet);
    link.addEventListener('click', event => {
      event.preventDefault();
      replaceUrl(`${location.pathname}${location.search}#${record.targetId}`);
      openTarget(record, event.shiftKey);
    });
    link.addEventListener('keydown', event => {
      if (event.key === 'Enter' && event.shiftKey) {
        event.preventDefault();
        replaceUrl(`${location.pathname}${location.search}#${record.targetId}`);
        openTarget(record, true);
      }
    });
    return link;
  };

  const editDistance = (a, b) => {
    const previous = Array.from({ length: b.length + 1 }, (_, index) => index);
    for (let i = 1; i <= a.length; i += 1) {
      const current = [i];
      for (let j = 1; j <= b.length; j += 1) {
        current[j] = Math.min(
          current[j - 1] + 1,
          previous[j] + 1,
          previous[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)
        );
      }
      previous.splice(0, previous.length, ...current);
    }
    return previous[b.length];
  };

  const suggestionVocabulary = [...new Set([
    ...searchRecords.flatMap(record => [record.title, record.headingTitle, record.topicTitle]),
    ...synonymGroups.flat()
  ].map(normalize).flatMap(value => value.split(' ')).filter(word => word.length >= 3))];

  const nearestSuggestions = query => {
    const token = normalize(query).split(' ').filter(Boolean).pop() || '';
    if (token.length < 3) return [];
    return suggestionVocabulary
      .map(term => ({ term, distance: editDistance(token, term) }))
      .filter(item => item.distance <= Math.max(2, Math.floor(token.length / 3)))
      .sort((a, b) => a.distance - b.distance || a.term.localeCompare(b.term))
      .slice(0, 5)
      .map(item => item.term);
  };

  const renderRelated = parsed => {
    relatedPanel.replaceChildren();
    const queryNorm = parsed.normalized;
    const key = Object.keys(relatedConcepts).find(candidate => queryNorm.includes(normalize(candidate)));
    if (!key) {
      relatedPanel.hidden = true;
      return;
    }
    const label = document.createElement('span');
    label.className = 'related-label';
    label.textContent = 'Related:';
    relatedPanel.appendChild(label);
    relatedConcepts[key].forEach(term => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'related-search';
      button.textContent = term;
      button.addEventListener('click', () => {
        searchInput.value = term;
        renderedLimit = 30;
        runSearch();
        searchInput.focus();
      });
      relatedPanel.appendChild(button);
    });
    relatedPanel.hidden = false;
  };

  const updateUrlState = () => {
    if (initializing) return;
    const url = new URL(window.location.href);
    const query = searchInput.value.trim();
    if (query) url.searchParams.set('q', query);
    else url.searchParams.delete('q');
    if (selectedType !== 'all') url.searchParams.set('type', selectedType);
    else url.searchParams.delete('type');
    if (scopeSelect.value !== 'all') url.searchParams.set('topic', scopeSelect.value);
    else url.searchParams.delete('topic');
    replaceUrl(`${url.pathname}${url.search}${url.hash}`);
  };

  const runSearch = () => {
    clearMarks();
    const parsed = parseQuery(searchInput.value);
    const scope = scopeSelect.value;
    const hasQuery = Boolean(parsed.raw);
    const hasFilter = selectedType !== 'all';
    const hasScope = scope !== 'all';

    const rawMatches = searchRecords
      .filter(record => scope === 'all' || record.topicId === scope)
      .filter(record => selectedType === 'all' || record.types.includes(selectedType))
      .filter(record => !hasQuery || parsed.groups.some(group => groupMatches(record, group)))
      .map(record => ({ ...record, score: scoreRecord(record, parsed) }))
      .sort((a, b) => b.score - a.score || a.topicTitle.localeCompare(b.topicTitle) || a.title.localeCompare(b.title));

    latestMatches = compactMatches(rawMatches);
    const rawMatchCount = rawMatches.length;
    const matchingTopicIds = new Set(rawMatches.map(record => record.topicId));
    topics.forEach(topic => {
      const show = (!hasQuery && !hasFilter && !hasScope) || matchingTopicIds.has(topic.id);
      topic.classList.toggle('is-hidden', !show);
      if (show && hasQuery) highlightTokens(topic, visiblePositiveTerms(parsed));
    });

    results.replaceChildren();
    currentResultIndex = -1;

    if (!hasQuery && !hasFilter && !hasScope) {
      status.textContent = `All ${topics.length} topics shown.`;
      relatedPanel.hidden = true;
      updateUrlState();
      return;
    }

    if (latestMatches.length) {
      const topicsCount = matchingTopicIds.size;
      const passageNote = rawMatchCount > latestMatches.length ? ` from ${rawMatchCount} matching passages` : '';
      status.textContent = `${latestMatches.length} ranked result${latestMatches.length === 1 ? '' : 's'}${passageNote} in ${topicsCount} topic${topicsCount === 1 ? '' : 's'}.`;
      latestMatches.slice(0, renderedLimit).forEach((record, index) => results.appendChild(renderResult(record, parsed, index)));
      if (latestMatches.length > renderedLimit) {
        const more = document.createElement('button');
        more.type = 'button';
        more.className = 'search-more';
        more.textContent = `Show ${Math.min(30, latestMatches.length - renderedLimit)} more`;
        more.addEventListener('click', () => {
          renderedLimit += 30;
          runSearch();
        });
        results.appendChild(more);
      }
      renderRelated(parsed);
    } else {
      status.textContent = `No result matches “${searchInput.value.trim() || selectedType}”.`;
      const hint = document.createElement('div');
      hint.className = 'search-empty';
      const message = document.createElement('p');
      message.textContent = 'Try removing a term, changing the result type, or using an acronym or broader concept.';
      hint.appendChild(message);
      const suggestions = nearestSuggestions(searchInput.value);
      if (suggestions.length) {
        const suggestionRow = document.createElement('div');
        suggestionRow.className = 'search-suggestions';
        const label = document.createElement('span');
        label.textContent = 'Closest terms:';
        suggestionRow.appendChild(label);
        suggestions.forEach(term => {
          const button = document.createElement('button');
          button.type = 'button';
          button.textContent = term;
          button.addEventListener('click', () => {
            searchInput.value = term;
            renderedLimit = 30;
            runSearch();
          });
          suggestionRow.appendChild(button);
        });
        hint.appendChild(suggestionRow);
      }
      results.appendChild(hint);
      relatedPanel.hidden = true;
    }

    updateUrlState();
  };

  const clearSearch = () => {
    searchInput.value = '';
    selectedType = 'all';
    scopeSelect.value = 'all';
    setSelectedType('all');
    renderedLimit = 30;
    runSearch();
    searchInput.focus();
  };

  const resultLinks = () => [...results.querySelectorAll('.search-result')];
  const focusResult = index => {
    const links = resultLinks();
    if (!links.length) return;
    currentResultIndex = (index + links.length) % links.length;
    links[currentResultIndex].focus();
  };

  searchInput.addEventListener('input', () => {
    renderedLimit = 30;
    runSearch();
  });
  searchInput.addEventListener('keydown', event => {
    if (event.key === 'ArrowDown') {
      event.preventDefault();
      focusResult(0);
    }
  });
  clearButton.addEventListener('click', clearSearch);
  scopeSelect.addEventListener('change', () => {
    renderedLimit = 30;
    runSearch();
  });
  filterGroup.addEventListener('click', event => {
    const button = event.target.closest('.search-filter');
    if (!button) return;
    setSelectedType(button.dataset.filter);
    renderedLimit = 30;
    runSearch();
  });
  results.addEventListener('keydown', event => {
    if (!event.target.matches('.search-result')) return;
    const links = resultLinks();
    const index = links.indexOf(event.target);
    if (event.key === 'ArrowDown') {
      event.preventDefault();
      focusResult(index + 1);
    } else if (event.key === 'ArrowUp') {
      event.preventDefault();
      if (index === 0) searchInput.focus();
      else focusResult(index - 1);
    } else if (event.key === 'Home') {
      event.preventDefault();
      focusResult(0);
    } else if (event.key === 'End') {
      event.preventDefault();
      focusResult(links.length - 1);
    }
  });

  topics.forEach(topic => {
    const sourceLinks = topic.querySelector('.source-links');
    if (!sourceLinks || sourceLinks.querySelector('.search-topic-button')) return;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'search-topic-button';
    button.textContent = 'Search this topic';
    button.addEventListener('click', () => {
      scopeSelect.value = topic.id;
      renderedLimit = 30;
      openMenu(true);
      runSearch();
    });
    sourceLinks.appendChild(button);
  });

  document.querySelectorAll('.toc a, .topic-map a').forEach(link => link.addEventListener('click', closeMenu));

  document.addEventListener('keydown', event => {
    const target = event.target;
    const typing = target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target.isContentEditable;
    if ((event.key === '/' && !typing) || ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k')) {
      event.preventDefault();
      openMenu(true);
    }
    if (event.key === 'Escape') {
      if (searchInput.value || selectedType !== 'all' || scopeSelect.value !== 'all') clearSearch();
      else if (!menuPanel.hidden) closeMenu();
    }
  });

  let savedTheme = null;
  try { savedTheme = localStorage.getItem('data785-theme'); } catch (_error) { /* Storage is optional. */ }
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
    try { localStorage.setItem('data785-theme', next); } catch (_error) { /* Storage is optional. */ }
    updateThemeLabel();
  });
  printButton.addEventListener('click', () => window.print());

  const params = new URLSearchParams(window.location.search);
  searchInput.value = params.get('q') || '';
  setSelectedType(params.get('type') || 'all');
  const requestedTopic = params.get('topic');
  if (requestedTopic && topics.some(topic => topic.id === requestedTopic)) scopeSelect.value = requestedTopic;
  initializing = false;
  runSearch();

  if (window.location.hash) {
    window.setTimeout(() => {
      const target = document.getElementById(window.location.hash.slice(1));
      if (target) target.scrollIntoView({ block: 'start' });
    }, 0);
  }
})();
