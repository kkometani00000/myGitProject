using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    internal static class CDictionary
    {
        public static void MainDictionary()
        {
            GetDictionary();
        }

        private static void GetDictionary()
        {
            var dic = new Dictionary<(int id, int subId), (string s, int n)>();
            dic.Add((1, 1), ("str11", 11));
            dic.Add((1, 2), ("str12", 12));
            dic.Add((1, 3), ("str13", 13));
            dic.Add((2, 1), ("str21", 21));
            dic.Add((2, 2), ("str22", 22));
            dic.Add((2, 3), ("str23", 23));

            // データ抽出
            (string s, int n) data = dic[(2, 2)];
        }
    }
}
