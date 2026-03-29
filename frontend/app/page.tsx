"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any>(null);

  const runQuery = async () => {
    const res = await axios.post("http://localhost:8000/query?q=" + query);
    setResults(res.data);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>Agentic Commerce</h1>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />

      <button onClick={runQuery}>Search</button>

      {results && (
        <div>
          <h2>Products</h2>
          {results.response.products.map((p: any, i: number) => (
            <div key={i}>
              <h3>{p.title}</h3>
              <p>${p.price}</p>
              <a href={p.affiliate}>Buy</a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
