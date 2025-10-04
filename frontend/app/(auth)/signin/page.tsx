import { Button } from "@/components/ui/button";

export default function SignInPage() {
  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-semibold">Sign in</h2>
      <Button onClick={() => alert("Auth stub")}>Continue</Button>
    </div>
  );
}


