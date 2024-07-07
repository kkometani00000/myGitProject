using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    //カリー化
    internal static class CCurrying
    {
        public static void MainCurrying()
        {
            int iCurrying1 = GetCurrying(10, 22);
            int num1 = Sum(3, 5); // 普通に、8

            // Sumをカリー化する、関数はデリゲートに包む必要がある
            var CurriedSum = Currying((Func<int, int, int>)Sum);
            int num2 = CurriedSum(3)(5); // 当然、8

            var BindedSum = CurriedSum(3); // 3を部分適用する
            int num3 = BindedSum(5); // 勿論、8

            var UnCurriedSum = UnCurrying(CurriedSum); // 非カリー化
            int num4 = UnCurriedSum(3, 5); // 当然、Sum関数と一緒
        }

        private static int GetCurrying(int data1, int data2)
        {
            Func<int, Func<int,　int>> f = x1 => x2 => x1 + x2;
            return f(data1)(data2);
        }

        // カリー化する関数
        private static Func<T, Func<U, V>> Currying<T, U, V>(Func<T, U, V> func)
        {
            return t => u => func(t, u);
        }

        // 非カリー化する関数
        private static Func<T, U, V> UnCurrying<T, U, V>(Func<T, Func<U, V>> func)
        {
            return (t, u) => func(t)(u);
        }

        // 例として使うx+yを返す関数
        private static int Sum(int x, int y)
        {
            return x + y;
        }

    }
}
