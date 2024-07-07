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
            dic.Add((1, 2), ("str", 0));
        }
    }
}
