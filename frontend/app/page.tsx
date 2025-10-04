import Link from "next/link";

export default function LandingPage() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-16">
        <section className="text-center mb-16">
          <h1 className="text-5xl font-bold text-gray-900 mb-6">AITube</h1>
          <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
            Automatically monitor YouTube channels, transcribe videos, and generate AI-powered summaries. 
            Never miss important content from your favorite creators.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link 
              href="/dashboard"
              className="bg-blue-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors"
            >
              Get Started
            </Link>
            <Link 
              href="/pricing"
              className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold border border-blue-600 hover:bg-blue-50 transition-colors"
            >
              View Pricing
            </Link>
          </div>
        </section>

        <section className="grid md:grid-cols-3 gap-8 mb-16">
          <div className="bg-white rounded-lg p-6 shadow-lg">
            <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
              <span className="text-2xl">📺</span>
            </div>
            <h3 className="text-xl font-semibold mb-2">Monitor Channels</h3>
            <p className="text-gray-600">
              Add your favorite YouTube channels and automatically track their latest videos.
            </p>
          </div>
          
          <div className="bg-white rounded-lg p-6 shadow-lg">
            <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4">
              <span className="text-2xl">🎤</span>
            </div>
            <h3 className="text-xl font-semibold mb-2">AI Transcription</h3>
            <p className="text-gray-600">
              Automatically transcribe video audio using advanced AI technology for accurate results.
            </p>
          </div>
          
          <div className="bg-white rounded-lg p-6 shadow-lg">
            <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
              <span className="text-2xl">🤖</span>
            </div>
            <h3 className="text-xl font-semibold mb-2">Smart Summaries</h3>
            <p className="text-gray-600">
              Get intelligent summaries with key points, hashtags, and keywords for each video.
            </p>
          </div>
        </section>

        <section className="bg-white rounded-lg p-8 shadow-lg">
          <h2 className="text-2xl font-bold text-center mb-6">How It Works</h2>
          <div className="grid md:grid-cols-4 gap-6">
            <div className="text-center">
              <div className="w-16 h-16 bg-blue-500 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">1</div>
              <h3 className="font-semibold mb-2">Add Channels</h3>
              <p className="text-sm text-gray-600">Add YouTube channels you want to monitor</p>
            </div>
            <div className="text-center">
              <div className="w-16 h-16 bg-green-500 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">2</div>
              <h3 className="font-semibold mb-2">Auto Monitor</h3>
              <p className="text-sm text-gray-600">System automatically checks for new videos</p>
            </div>
            <div className="text-center">
              <div className="w-16 h-16 bg-purple-500 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">3</div>
              <h3 className="font-semibold mb-2">AI Processing</h3>
              <p className="text-sm text-gray-600">Videos are transcribed and summarized</p>
            </div>
            <div className="text-center">
              <div className="w-16 h-16 bg-orange-500 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">4</div>
              <h3 className="font-semibold mb-2">Get Insights</h3>
              <p className="text-sm text-gray-600">View summaries and key insights instantly</p>
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}


