import { ReactNode } from "react";

export default function AuthLayout({ children }: { children: ReactNode }) {
  return <div className="max-w-md mx-auto py-16">{children}</div>;
}


