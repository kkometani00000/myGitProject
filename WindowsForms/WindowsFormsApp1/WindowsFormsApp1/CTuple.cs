using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    internal static class CTuple
    {
        public static void MainTuple()
        {
            var tData = CTuple.GetTuple("99");
            var tuple = (10, 20);
            CTuple.UpdateTuple(tuple); // 引数としてタプルを渡す
        }

        private static Tuple<int, bool> GetTuple(string data)
        {
            int iData;
            bool bResult = int.TryParse(data, out iData);
            return Tuple.Create(iData, bResult);
        }

        private static void UpdateTuple((int, int) tuple)
        {
            tuple.Item1 = 300;
            tuple.Item2 = 400;
            Debug.WriteLine("");
            Debug.WriteLine($"Updated! : {tuple}");
        }

    }
}
