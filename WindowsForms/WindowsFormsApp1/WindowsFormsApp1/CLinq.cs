using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Collections;

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
            //var list = new List<int> { 1, 84, 95, 95, 40, 6 };
            var list = new List<int> { 6, 95, 95, 84 ,1 ,40 };

            // クエリ式
            var query = from x in list
                        where x % 2 == 0
                        orderby x
                        select x * 3;

            // ラムダ式
            var query2 = list.Where(x => x % 2 == 0).Select(x => x * 3).OrderBy(x => x);

            // foreach
            List<int> result = new List<int>();
            foreach (var x in list)
            {
                if ((x % 2) != 0) continue;
                int data = x * 3;
                var y = result.Select((v, i) => new { data = v, index = i }).Where(v => data <= v.data).FirstOrDefault();
                if (y != null) result.Insert(y.index, data);
                else result.Add(data);
            }

            Debug.WriteLine("");
            Debug.WriteLine("GetLinq1");
            Debug.WriteLine("クエリ式：" + CCommon<int>.GetStrJoin(query.ToList()));
            Debug.WriteLine("ラムダ式：" + CCommon<int>.GetStrJoin(query2.ToList()));
            Debug.WriteLine("foreach：" + CCommon<int>.GetStrJoin(result));
        }

        private static void GetLinq2()
        {
            var list = new List<int> { 1, 84, 95, 95, 40, 6 };

            Debug.WriteLine("");
            Debug.WriteLine("GetLinq2");
            
            Debug.WriteLine("Max: " + list.Max());          // list の最大値を取得
            Debug.WriteLine("Min: " + list.Min());          // list の最小値を取得
            Debug.WriteLine("Average: " + list.Average());  // list の平均値を取得
            Debug.WriteLine("Sum: " + list.Sum());          // list の合計値を取得
            Debug.WriteLine("Count: " + list.Count());      // list の要素値を取得

            Debug.WriteLine("All: " + list.All(x => x < 100));      // list のすべての要素が 100 未満かどうか
            Debug.WriteLine("Any: " + list.Any(x => x < 0));        // list のいずれかの要素が 0 未満かどうか
            Debug.WriteLine("Contains: " + list.Contains(40));      // list に値が 40 の要素が含まれてるかどうか
        }

        private static void GetLinq3()
        {
            var list = new List<int> { 1, 84, 95, 95, 40, 6 };

            Debug.WriteLine("");
            Debug.WriteLine("GetLinq3");

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
