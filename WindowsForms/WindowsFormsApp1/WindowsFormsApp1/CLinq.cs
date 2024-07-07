using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    internal static class CLinq
    {
        public static void MainLinq()
        {
            GetLinq1();
            GetLinq2();
            GetLinq3();
            GetLinq4();
        }

        private static void GetLinq1()
        {
            var list = new List<int> { 1, 84, 95, 95, 40, 6 };

            var query = from x in list
                        where x % 2 == 0
                        orderby x
                        select x * 3;

            Debug.WriteLine("");
            Debug.WriteLine("GetLinq1");
            Debug.WriteLine(CCommon<int>.GetStrJoin(query.ToList()));
        }

        private static void GetLinq2()
        {
            var list = new List<int> { 1, 84, 95, 95, 40, 6 };

            Debug.WriteLine("");
            Debug.WriteLine("GetLinq2");

            // list の最大値を取得
            Debug.WriteLine("Max: " + list.Max());

            // list の最小値を取得
            Debug.WriteLine("Min: " + list.Min());

            // list の平均値を取得
            Debug.WriteLine("Average: " + list.Average());

            // list の合計値を取得
            Debug.WriteLine("Sum: " + list.Sum());

            // list の要素値を取得
            Debug.WriteLine("Count: " + list.Count());
        }

        private static void GetLinq3()
        {
            var list = new List<int> { 1, 84, 95, 95, 40, 6 };

            Debug.WriteLine("");
            Debug.WriteLine("GetLinq3");

            // list のすべての要素が 100 未満かどうか
            Console.WriteLine("All: " + list.All(x => x < 100));

            // list のいずれかの要素が 0 未満かどうか
            Console.WriteLine("Any: " + list.Any(x => x < 0));

            // list に値が 40 の要素が含まれてるかどうか
            Console.WriteLine("Contains: " + list.Contains(40));
        }

        private static void GetLinq4()
        {
            var list0 = new List<int> { 1, 84, 95, 95, 40, 6 };
            var list = list0.Select((x, i) => new { data=x, index=i }).ToList();

            Debug.WriteLine("");
            Debug.WriteLine("GetLinq4");

            foreach (var data in list)
            {
                // list のすべての要素が 100 未満かどうか
                Console.WriteLine($"data: {data}");
            }

        }
    }
}
