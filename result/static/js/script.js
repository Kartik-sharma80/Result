window.onload = function () {
    document.getElementById("download")
        .addEventListener("click", () => {
            const invoice = this.document.getElementById("invoice");
            console.log(invoice);
            console.log(window);
             var opt = {
                margin: 0,
                filename: 'result.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 1, scrollY: 0},
                jsPDF: { unit: 'in', format: 'legal', orientation: 'portrait' }
            };
            html2pdf().from(invoice).set(opt).save();
        })
}
