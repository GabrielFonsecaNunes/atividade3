function copyCode(containerId) {
    var container = document.getElementById(containerId);
    var textarea = container.querySelector('textarea');
    textarea.select();
    document.execCommand('copy');
    alert('Código copiado para a área de transferência!');
}

function copyCodeFromFile() {
    var code = document.querySelector("pre").textContent;
    var input = document.createElement("input");
    input.value = code;
    input.type = "text";
    input.style.display = "none";
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    document.body.removeChild(input);
    alert("Code copied to clipboard!");
}