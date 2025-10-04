export default function PricingPage() {
  return (
    <main>
      <h2 className="text-2xl font-semibold">Pricing</h2>
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-6">
        <div className="border rounded p-6">
          <h3 className="font-medium">Free</h3>
          <p className="text-sm text-slate-500">Basic summaries</p>
        </div>
        <div className="border rounded p-6">
          <h3 className="font-medium">Pro</h3>
          <p className="text-sm text-slate-500">Advanced summaries</p>
        </div>
        <div className="border rounded p-6">
          <h3 className="font-medium">Team</h3>
          <p className="text-sm text-slate-500">Collaboration features</p>
        </div>
      </div>
    </main>
  );
}


