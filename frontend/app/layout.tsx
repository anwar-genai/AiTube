import "../styles/globals.css";
import { ReactNode } from "react";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-white text-slate-900">
        <nav className="border-b">
          <div className="max-w-5xl mx-auto px-4 h-12 flex items-center gap-4">
            <a href="/" className="font-semibold">AITube</a>
            <a href="/pricing" className="text-sm text-slate-600">Pricing</a>
            <a href="/dashboard" className="text-sm text-slate-600">Dashboard</a>
            <a href="/(auth)/signin" className="ml-auto text-sm">Sign in</a>
          </div>
        </nav>
        <div className="max-w-5xl mx-auto px-4 py-8">{children}</div>
      </body>
    </html>
  );
}


