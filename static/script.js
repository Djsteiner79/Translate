async function translateText() {
    const sourceLanguage = document.getElementById("sourceLanguage").value;
    const targetLanguage = document.getElementById("targetLanguage").value;
    const inputText = document.getElementById("inputText").value;

    try {
        const response = await fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                sourceLanguage: sourceLanguage,
                targetLanguage: targetLanguage,
                text: inputText
            })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Something went wrong');
        }

        const data = await response.json();
        document.getElementById("outputText").value = data.translatedText;
    } catch (error) {
        document.getElementById("outputText").value = `Error: ${error.message}`;
    }
}
