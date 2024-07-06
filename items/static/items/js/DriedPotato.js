(function() {
  function getDateTimeString() {
    let today = new Date();
    let year = today.getFullYear();
    let month = ("0" + String(today.getMonth() + 1)).slice(-2);
    let day = ("0" + String(today.getDate())).slice(-2);
    let hour = ("0" + String(today.getHours())).slice(-2);
    let minute = ("0" + String(today.getMinutes())).slice(-2);
    let second = ("0" + String(today.getSeconds())).slice(-2);

    return " " + year + month + day + hour + minute + second;
  };

  const border = {
    border: {
      top: { style: "thin" },
      bottom: { style: "thin" },
      left: { style: "thin" },
      right: { style: "thin" }
    }
  };

  let download = document.querySelector("#download-button");

  if(download) {
    download.addEventListener('click', function() {
      let table = document.querySelector("#wishlist");
      let wb = XLSX.utils.table_to_book(table); 
      let sh = wb.Sheets["Sheet1"];
      let filename = "wishlist-" + getDateTimeString() + ".xlsx";

      for(const rangeName in sh) {
        if (rangeName.indexOf('!') === 0) {
          continue;
        }

        delete sh[rangeName].l; // disable hyperlink
        sh[rangeName].s = border;
      }
      XLSX.writeFile(wb, filename); 
    });
  }
}());
