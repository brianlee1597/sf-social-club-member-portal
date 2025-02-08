import { useRouterWithOptimisticPathname } from "@/app/hooks/useOptimisticRouter";
import Cookies from "js-cookie";
import Link from "next/link";
import { UserIcon } from '@heroicons/react/24/outline';
import { userApi } from "@/lib/user/userApi";
import { useAppSelector } from "@/lib/hooks";

export const Avatar = () => {
    const router = useRouterWithOptimisticPathname();
    const userId = useAppSelector(state => state.auth.userId)
    const { data: apiData } = userApi.useGetUserQuery(userId!, { skip: !userId });

    // TODO: Need UX
    const handleLogoutClick = () => {
        Cookies.remove('access_token')
        router.push('/login')
    }

    return (
            <Link href="/" className="btn btn-ghost btn-circle avatar" >
                {!apiData?.photo ? <UserIcon className="size-7" /> : <img
                    alt="avatar"
                    src={apiData.photo} />}
            </Link>
        )
}