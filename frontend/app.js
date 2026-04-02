async function loadInsights() {
  const res = await fetch("http://127.0.0.1:8000/insights/");
  const data = await res.json();

  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}
