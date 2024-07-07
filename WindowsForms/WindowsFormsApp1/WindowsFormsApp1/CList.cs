using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    internal static class CList
    {
        //複数の型を持つ変数
        private static (int x, int y) value;

        public static void MainList()
        {
            var lData = GetList();
        }

        private static List<(string s, int n)> GetList()
        {
            var list = new List<(string s, int n)>();
            list.Add(("str0", 0));
            list.Add(("str1", 1));
            list.Add(("str2", 2));

            //foreachで要素を受け取る
            foreach (var (s, n) in list) { }

            //Listなどの要素
            var listx = new List<(string s, int n)>();

            // foreachで要素を受け取る
            return list.Select(x => x).ToList();
        }
    }
}
