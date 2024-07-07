using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    internal static class CCommon<T>
    {
        public static string GetStrJoin(List<T> list)
        {
            return string.Join(",", list);
        }
    }
}
