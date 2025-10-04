"use client";

import { useEffect, useState } from "react";

type Summary = {
  id: number;
  video_id: number;
  summary_text: string;
  hashtags?: string;
  keywords?: string;
};

type Channel = {
  id: number;
  title: string;
  external_id: string;
  platform: string;
  created_at: string;
};

type Video = {
  id: number;
  title: string;
  description: string;
  thumbnail_url?: string;
  created_at: string;
};

export default function DashboardPage() {
  const [summaries, setSummaries] = useState<Summary[]>([]);
  const [channels, setChannels] = useState<Channel[]>([]);
  const [videos, setVideos] = useState<Video[]>([]);
  const [loading, setLoading] = useState(false);
  const [newChannel, setNewChannel] = useState({
    title: "",
    external_id: "",
    platform: "youtube"
  });
  
  const backend = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8001";

  useEffect(() => {
    fetchData();
  }, [backend]);

  const fetchData = async () => {
    try {
      const [summariesRes, channelsRes, videosRes] = await Promise.all([
        fetch(`${backend}/summaries`),
        fetch(`${backend}/channels`),
        fetch(`${backend}/videos`)
      ]);
      
      setSummaries(await summariesRes.json());
      setChannels(await channelsRes.json());
      setVideos(await videosRes.json());
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const addChannel = async () => {
    if (!newChannel.title || !newChannel.external_id) {
      alert("Please fill in both title and channel ID");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch(`${backend}/channels/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          owner_id: 1,
          external_id: newChannel.external_id,
          platform: newChannel.platform,
          title: newChannel.title
        })
      });

      if (response.ok) {
        alert("Channel added successfully!");
        setNewChannel({ title: "", external_id: "", platform: "youtube" });
        fetchData();
      } else {
        const error = await response.text();
        alert(`Error: ${error}`);
      }
    } catch (error) {
      alert(`Error: ${error}`);
    } finally {
      setLoading(false);
    }
  };

  const startMonitoring = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${backend}/monitor/start`, {
        method: "POST"
      });

      if (response.ok) {
        alert("Monitoring started! Videos are being processed...");
        setTimeout(fetchData, 3000); // Refresh data after 3 seconds
      } else {
        const error = await response.text();
        alert(`Error: ${error}`);
      }
    } catch (error) {
      alert(`Error: ${error}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="p-6 max-w-6xl mx-auto">
      <h1 className="text-3xl font-bold mb-8">AITube Dashboard</h1>
      
      {/* Add Channel Section */}
      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <h2 className="text-xl font-semibold mb-4">Add YouTube Channel</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <input
            type="text"
            placeholder="Channel Name (e.g., freeCodeCamp.org)"
            value={newChannel.title}
            onChange={(e) => setNewChannel({...newChannel, title: e.target.value})}
            className="border rounded px-3 py-2"
          />
          <input
            type="text"
            placeholder="Channel ID (e.g., UC8butISFwT-Wl7EV0hUK0BQ)"
            value={newChannel.external_id}
            onChange={(e) => setNewChannel({...newChannel, external_id: e.target.value})}
            className="border rounded px-3 py-2"
          />
          <button
            onClick={addChannel}
            disabled={loading}
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:opacity-50"
          >
            {loading ? "Adding..." : "Add Channel"}
          </button>
        </div>
        
        {/* Quick Add Popular Channels */}
        <div className="mt-4">
          <p className="text-sm text-gray-600 mb-2">Quick add popular channels:</p>
          <div className="flex flex-wrap gap-2">
            <button
              onClick={() => setNewChannel({
                title: "freeCodeCamp.org",
                external_id: "UC8butISFwT-Wl7EV0hUK0BQ",
                platform: "youtube"
              })}
              className="text-xs bg-gray-100 px-2 py-1 rounded hover:bg-gray-200"
            >
              FreeCodeCamp
            </button>
            <button
              onClick={() => setNewChannel({
                title: "Marques Brownlee",
                external_id: "UCBJycsmduvYEL83R_U4JriQ",
                platform: "youtube"
              })}
              className="text-xs bg-gray-100 px-2 py-1 rounded hover:bg-gray-200"
            >
              MKBHD
            </button>
            <button
              onClick={() => setNewChannel({
                title: "Traversy Media",
                external_id: "UCuAXFkgsw1L7xaCfnd5JJOw",
                platform: "youtube"
              })}
              className="text-xs bg-gray-100 px-2 py-1 rounded hover:bg-gray-200"
            >
              Traversy Media
            </button>
          </div>
        </div>
      </div>

      {/* Monitoring Section */}
      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <h2 className="text-xl font-semibold mb-4">Channel Monitoring</h2>
        <div className="flex items-center gap-4">
          <button
            onClick={startMonitoring}
            disabled={loading}
            className="bg-green-500 text-white px-6 py-2 rounded hover:bg-green-600 disabled:opacity-50"
          >
            {loading ? "Processing..." : "Start Monitoring All Channels"}
          </button>
          <span className="text-sm text-gray-600">
            This will fetch and process videos from all added channels
          </span>
        </div>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-blue-50 rounded-lg p-4">
          <h3 className="font-semibold text-blue-800">Channels</h3>
          <p className="text-2xl font-bold text-blue-600">{channels.length}</p>
        </div>
        <div className="bg-green-50 rounded-lg p-4">
          <h3 className="font-semibold text-green-800">Videos</h3>
          <p className="text-2xl font-bold text-green-600">{videos.length}</p>
        </div>
        <div className="bg-purple-50 rounded-lg p-4">
          <h3 className="font-semibold text-purple-800">Summaries</h3>
          <p className="text-2xl font-bold text-purple-600">{summaries.length}</p>
        </div>
      </div>

      {/* Channels List */}
      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <h2 className="text-xl font-semibold mb-4">Your Channels ({channels.length})</h2>
        <div className="space-y-2">
          {channels.map((channel) => (
            <div key={channel.id} className="flex justify-between items-center p-3 border rounded">
              <div>
                <h3 className="font-medium">{channel.title}</h3>
                <p className="text-sm text-gray-500">{channel.external_id}</p>
              </div>
              <span className="text-xs text-gray-400">
                {new Date(channel.created_at).toLocaleDateString()}
              </span>
            </div>
          ))}
          {channels.length === 0 && (
            <p className="text-gray-500 text-center py-4">No channels added yet</p>
          )}
        </div>
      </div>

      {/* Videos List */}
      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <h2 className="text-xl font-semibold mb-4">Recent Videos ({videos.length})</h2>
        <div className="space-y-4">
          {videos.slice(0, 5).map((video) => (
            <div key={video.id} className="flex gap-4 p-3 border rounded">
              {video.thumbnail_url && (
                <img 
                  src={video.thumbnail_url} 
                  alt={video.title}
                  className="w-24 h-18 object-cover rounded"
                />
              )}
              <div className="flex-1">
                <h3 className="font-medium">{video.title}</h3>
                <p className="text-sm text-gray-600 line-clamp-2">{video.description}</p>
                <p className="text-xs text-gray-400 mt-1">
                  {new Date(video.created_at).toLocaleDateString()}
                </p>
              </div>
            </div>
          ))}
          {videos.length === 0 && (
            <p className="text-gray-500 text-center py-4">No videos processed yet</p>
          )}
        </div>
      </div>

      {/* Summaries Feed */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-4">AI Summaries ({summaries.length})</h2>
        <div className="space-y-4">
          {summaries.map((s) => (
            <article key={s.id} className="border rounded p-4">
              <p className="whitespace-pre-wrap text-sm">{s.summary_text || "(empty)"}</p>
              {s.hashtags && <p className="text-xs mt-2 text-slate-500">{s.hashtags}</p>}
            </article>
          ))}
          {summaries.length === 0 && <p className="text-slate-500">No summaries yet.</p>}
        </div>
      </div>
    </main>
  );
}


