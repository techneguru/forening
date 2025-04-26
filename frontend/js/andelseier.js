document.querySelectorAll('iframe').forEach(iframe => {
  // Hide iframe initially
  iframe.style.display = 'none';
  // Add spinner
  const spinner = document.createElement('div');
  spinner.className = 'spinner';
  spinner.innerHTML = '<div class="spinner-inner"></div>';
  iframe.parentNode.insertBefore(spinner, iframe);

  iframe.addEventListener('load', () => {
    spinner.style.display = 'none';
    iframe.style.display = 'block';
  });
});
