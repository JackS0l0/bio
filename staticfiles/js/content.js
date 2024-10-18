document.addEventListener('visibilitychange', function () {
    if (document.hidden) {
        document.body.style.display = 'none'; // Məzmunu gizlədir
        alert('Ekran görüntüsü cəhdi aşkar edildi!'); // İstifadəçini xəbərdar edir
    } else {
        document.body.style.display = 'block'; // Yenidən göstərir
    }
});
