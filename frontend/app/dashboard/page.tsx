"use client";

import { useEffect, useState } from "react";

type Summary = {
  id: number;
  video_id: number;
  summary_text: string;
  hashtags?: string;
  keywords?: string;
};

export default function DashboardPage() {
  const [summaries, setSummaries] = useState<Summary[]>([]);
  const backend = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

  useEffect(() => {
    fetch(`${backend}/summaries`)
      .then((r) => r.json())
      .then(setSummaries)
      .catch(() => setSummaries([]));
  }, [backend]);

  return (
    <main>
      <h2 className="text-2xl font-semibold">Your Feed</h2>
      <div className="mt-6 space-y-4">
        {summaries.map((s) => (
          <article key={s.id} className="border rounded p-4">
            <p className="whitespace-pre-wrap text-sm">{s.summary_text || "(empty)"}</p>
            {s.hashtags && <p className="text-xs mt-2 text-slate-500">{s.hashtags}</p>}
          </article>
        ))}
        {summaries.length === 0 && <p className="text-slate-500">No summaries yet.</p>}
      </div>
    </main>
  );
}


