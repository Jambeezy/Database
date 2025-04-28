function copyToClipboard(text, button) {
    navigator.clipboard.writeText(text).then(() => {
        const originalText = button.textContent;
        button.textContent = 'Скопировано!';
        button.classList.remove('btn-primary');
        button.classList.add('btn-success');
        
        setTimeout(() => {
            button.textContent = originalText;
            button.classList.remove('btn-success');
            button.classList.add('btn-primary');
        }, 2000);
    }).catch(err => {
        console.error('Ошибка при копировании:', err);
    });
} 