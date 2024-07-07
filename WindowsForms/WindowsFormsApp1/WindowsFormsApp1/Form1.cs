using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // カリー化
            CCurrying.MainCurrying();

            // DataTable
            CDataTable.MainDataTable();

            // Tuple
            CTuple.MainTuple();

            // List
            CList.MainList();

            // Dictionary
            CDictionary.MainDictionary();

            // Tack
            CTack.MainTask();

            // Thread
            CThread.MainThread();

            // Linq
            CLinq.MainLinq();

            // Serialize Json
            CSerialize.MainSerialize();

        }

    }
}
