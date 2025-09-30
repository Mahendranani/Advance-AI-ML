const fetchData = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve({ data: "Sample Data", status: 200 });
        }, 1000);
    });
};

async function processData() {
    try {
        console.log("Fetching data...");
        const response = await fetchData();
        console.log("Data received:", response);
    } catch (error) {
        console.error("Error:", error);
    }
}

processData();