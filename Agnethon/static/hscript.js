function updateContactDetails() {
    var committee = document.getElementById('committee').value;
    var presidentNameInput = document.getElementById('presidentName');
    var presidentNumberInput = document.getElementById('presidentNumber');
    var vpNameInput = document.getElementById('vpName');
    var vpNumberInput = document.getElementById('vpNumber');

    if (committee === 'committeeA') {
        presidentNameInput.readOnly = false;
        presidentNumberInput.readOnly = false;
        vpNameInput.readOnly = false;
        vpNumberInput.readOnly = false;

        presidentNameInput.value = 'President A';
        presidentNumberInput.value = '1234567890';
        vpNameInput.value = 'Vice-President A';
        vpNumberInput.value = '0987654321';
    } else if (committee === 'committeeB') {
        presidentNameInput.readOnly = false;
        presidentNumberInput.readOnly = false;
        vpNameInput.readOnly = false;
        vpNumberInput.readOnly = false;

        presidentNameInput.value = 'President B';
        presidentNumberInput.value = '1234567890';
        vpNameInput.value = 'Vice-President B';
        vpNumberInput.value = '0987654321';
    } else if (committee === 'committeeC') {
        presidentNameInput.readOnly = false;
        presidentNumberInput.readOnly = false;
        vpNameInput.readOnly = false;
        vpNumberInput.readOnly = false;

        presidentNameInput.value = 'President C';
        presidentNumberInput.value = '1234567890';
        vpNameInput.value = 'Vice-President C';
        vpNumberInput.value = '0987654321';
    }
}
