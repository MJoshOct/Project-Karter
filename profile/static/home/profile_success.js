<script>
  window.addEventListener('DOMContentLoaded', (event) => {
    const toast = document.getElementById('toast');
    if (toast) {
      toast.style.display = 'block';
      setTimeout(() => {
        toast.style.opacity = '1';
      }, 100);

      // Hide after 3 seconds
      setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => { toast.style.display = 'none'; }, 500);
      }, 3000);
    }
  });
</script>
