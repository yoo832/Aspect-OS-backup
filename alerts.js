function copyErr1() {
  /* Get the text field */
  var copyText = document.getElementById("error2");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText.value);

  /* Alert the copied text */
  alert("Copied the text: " + copyText.value);
  alert(
    "Have a nice day! (Tip: Try press Ctrl Shift F5 to hard reload page OR do Ctrl Shift T to back your history)"
  );
}
