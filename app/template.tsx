"use client";

import Cookies from "js-cookie";

import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import LoadingPage from "./components/global/loadingPage";
import { useLazyGetRoleQuery } from "@/lib/services/role";
import { isFetchBaseQueryError } from "@/lib/services/functions/isBaseQueryError";

export default function Template({ children }: { children: React.ReactNode }) {
  const [loading, setLoading] = useState(true);
  const pathname = usePathname();
  const router = useRouter();

  // 1. Specify protected and public routes
  const protectedRoutes = ["/admin", "/member"];
  const publicRoutes = ["/login", "/"];

  const [getRole] = useLazyGetRoleQuery();

  useEffect(() => {
    const checkAuth = async () => {
      setLoading(true);
      // 2. Check if the current route is protected or public
      const isProtectedRoute = protectedRoutes.includes(pathname);
      const isPublicRoute = publicRoutes.includes(pathname);
      const isAdminRoute = pathname === "/admin";

      // 3. Obtain the session from the cookie
      const accessToken = Cookies.get("access_token");

      // 4. Redirect to /login if the user is not authenticated
      if (!accessToken) {
        if (pathname !== "/login") router.push("/login");
        return;
      }

      const { data: response, error } = await getRole(accessToken);

      setLoading(false);

      if (isFetchBaseQueryError(error) && error.status === 401) {
        router.push("/login");
        return;
      }

      // 5. Redirect to /login if role could not be retrieved from request
      if (isProtectedRoute && !response?.role) {
        router.push("/login");
        return;
      }

      // 6. Redirect admin route attempt for a non-admin user to /member
      if (isAdminRoute && response?.role !== "admin") {
        router.push("/member");
        return;
      }

      // 7. Redirect public routes to role route if the user is authenticated
      if (isPublicRoute && response?.role) {
        router.push(`/${response?.role}`);
        return;
      }
    };

    checkAuth();
  }, [pathname]);

  // Render the loading component while checking auth on non-login routes
  return loading && pathname !== "/login" ? <LoadingPage /> : <>{children}</>;
}
