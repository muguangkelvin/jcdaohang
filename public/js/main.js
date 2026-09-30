document.addEventListener('DOMContentLoaded', function() {
  // Mobile Menu Toggle
  const menuToggle = document.getElementById('menuToggle');
  const navLinks = document.getElementById('navLinks');
  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', function() {
      navLinks.classList.toggle('show');
    });
  }

  // Coupon Copy Functionality
  const copyButtons = document.querySelectorAll('.btn-copy-coupon');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      const code = this.getAttribute('data-code');
      if (!code) return;
      if (navigator.clipboard) {
        navigator.clipboard.writeText(code).then(() => {
          alert('优惠码 [' + code + '] 已成功复制到剪贴板！');
        }).catch(err => {
          prompt('请手动复制优惠码：', code);
        });
      } else {
        prompt('请手动复制优惠码：', code);
      }
    });
  });

  // Full-Site Interactive Search System
  const searchInput = document.getElementById('searchInput');
  const searchModal = document.getElementById('searchModal');
  const modalSearchInput = document.getElementById('modalSearchInput');
  const searchModalClose = document.getElementById('searchModalClose');
  const searchModalBackdrop = document.getElementById('searchModalBackdrop');
  const searchResultsBody = document.getElementById('searchResultsBody');

  let searchIndex = null;
  let isLoadingIndex = false;

  function loadSearchIndex(callback) {
    if (searchIndex) {
      if (callback) callback();
      return;
    }
    if (isLoadingIndex) return;
    isLoadingIndex = true;

    fetch('/index.json')
      .then(res => res.json())
      .then(data => {
        searchIndex = data;
        isLoadingIndex = false;
        if (callback) callback();
      })
      .catch(err => {
        console.error('Failed to load search index:', err);
        isLoadingIndex = false;
      });
  }

  function openSearchModal(initialQuery = '') {
    if (!searchModal) return;
    searchModal.classList.add('active');
    searchModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    if (modalSearchInput) modalSearchInput.focus();

    loadSearchIndex(() => {
      const q = initialQuery || (modalSearchInput ? modalSearchInput.value.trim() : '');
      if (q && modalSearchInput) {
        modalSearchInput.value = q;
      }
      performSearch(q);
    });
  }

  function closeSearchModal() {
    if (!searchModal) return;
    searchModal.classList.remove('active');
    searchModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  if (searchInput) {
    searchInput.addEventListener('click', function() {
      openSearchModal(this.value.trim());
    });
    searchInput.addEventListener('focus', function() {
      openSearchModal(this.value.trim());
    });
    searchInput.addEventListener('input', function() {
      openSearchModal(this.value.trim());
    });
  }

  if (searchModalClose) {
    searchModalClose.addEventListener('click', closeSearchModal);
  }
  if (searchModalBackdrop) {
    searchModalBackdrop.addEventListener('click', closeSearchModal);
  }

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && searchModal && searchModal.classList.contains('active')) {
      closeSearchModal();
    }
  });

  let debounceTimer = null;
  if (modalSearchInput) {
    modalSearchInput.addEventListener('input', function() {
      const q = this.value.trim();
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        performSearch(q);
      }, 120);
    });
  }

  function sectionToLabel(sec) {
    const map = {
      'picks': '优质推荐',
      'tutorials': '小白教程',
      'clients': '客户端下载',
      'iplc-gaming': '专线加速',
      'streaming': '流媒体/AI',
      'faq': 'FAQ问答',
      'providers': '机场评测'
    };
    return map[sec] || '核心指南';
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  function highlightMatches(text, query) {
    if (!query || !text) return text;
    const regex = new RegExp('(' + escapeRegExp(query) + ')', 'gi');
    return text.replace(regex, '<mark>$1</mark>');
  }

  function performSearch(query) {
    if (!searchResultsBody) return;

    if (!query) {
      searchResultsBody.innerHTML = `
        <div class="search-modal-placeholder">
          <p>🔍 请输入关键词（例如：<strong>灵动云</strong>、<strong>Clash</strong>、<strong>IPLC专线</strong>、<strong>ChatGPT</strong>、<strong>折合7元</strong>等）</p>
        </div>`;
      return;
    }

    if (!searchIndex) {
      searchResultsBody.innerHTML = `
        <div class="search-modal-placeholder">
          <p>⏳ 正在加载全站 191+ 篇文章与教程索引，请稍候...</p>
        </div>`;
      return;
    }

    const q = query.toLowerCase();
    const keywordsList = q.split(/\s+/).filter(Boolean);
    const scored = [];

    searchIndex.forEach(item => {
      const titleLower = (item.title || '').toLowerCase();
      const descLower = (item.description || '').toLowerCase();
      const kwLower = (item.keywords || '').toLowerCase();
      const tagsLower = (item.tags || '').toLowerCase();
      const contentLower = (item.content || '').toLowerCase();

      let score = 0;
      let matchedCount = 0;

      keywordsList.forEach(kw => {
        if (titleLower.includes(kw)) {
          score += 100;
          matchedCount++;
        }
        if (kwLower.includes(kw) || tagsLower.includes(kw)) {
          score += 50;
          matchedCount++;
        }
        if (descLower.includes(kw)) {
          score += 30;
          matchedCount++;
        }
        if (contentLower.includes(kw)) {
          score += 10;
          matchedCount++;
        }
      });

      if (score > 0) {
        scored.push({
          item: item,
          score: score,
          matchedCount: matchedCount
        });
      }
    });

    scored.sort((a, b) => b.score - a.score);

    if (scored.length === 0) {
      searchResultsBody.innerHTML = `
        <div class="search-modal-placeholder">
          <p>⚠️ 未检索到与 “<strong>${escapeHtml(query)}</strong>” 相关的文章。</p>
          <p style="margin-top:8px; font-size:0.85rem; color:#94a3b8;">小贴士：请尝试缩短关键词，或检索常见词（如 Clash、灵动云、iOS小火箭、IPLC专线）。</p>
        </div>`;
      return;
    }

    let html = `
      <div class="search-stats-bar">
        <span>全站共检索出 <strong>${scored.length}</strong> 篇相关文章/教程</span>
        <span>搜索词：<strong style="color:#2563eb;">${escapeHtml(query)}</strong></span>
      </div>`;

    scored.slice(0, 35).forEach(res => {
      const p = res.item;
      const tagLabel = sectionToLabel(p.section);
      
      let snippet = p.description || p.content || '';
      const matchIdx = snippet.toLowerCase().indexOf(q);
      if (matchIdx > -1) {
        const start = Math.max(0, matchIdx - 35);
        const end = Math.min(snippet.length, matchIdx + 85);
        snippet = (start > 0 ? '...' : '') + snippet.substring(start, end) + (end < snippet.length ? '...' : '');
      } else {
        snippet = snippet.substring(0, 110) + (snippet.length > 110 ? '...' : '');
      }

      const highlightedTitle = highlightMatches(escapeHtml(p.title), query);
      const highlightedSnippet = highlightMatches(escapeHtml(snippet), query);

      html += `
        <a href="${p.permalink}" class="search-result-item">
          <div class="search-result-header">
            <span class="search-result-tag">${tagLabel}</span>
            <span class="search-result-title">${highlightedTitle}</span>
          </div>
          <div class="search-result-snippet">${highlightedSnippet}</div>
        </a>`;
    });

    if (scored.length > 35) {
      html += `<div style="text-align:center; padding:12px; font-size:0.85rem; color:#64748b;">更多匹配项未能完全展示，请输入更精准的关键词匹配</div>`;
    }

    searchResultsBody.innerHTML = html;
  }
});
