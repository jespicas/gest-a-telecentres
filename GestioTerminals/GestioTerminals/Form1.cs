using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Net.NetworkInformation;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace GestioTerminals
{
    public partial class Form1 : Form
    {

        Ping netMon = new Ping();
        Thread tre; 
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            tre = new Thread(new ThreadStart(StartListening));
            tre.Start();
        }
        delegate void AfegirChekcBoxCallback(string paremeter);

        public void AddCheckBox(string strQue)
        {
            bool trobat = false;
            if (this.listView1.InvokeRequired)
            {
                AfegirChekcBoxCallback d = new AfegirChekcBoxCallback(AddCheckBox);
                this.Invoke(d, new object[] { strQue });
            }
            else
            {
                ListViewItem li = new ListViewItem("pc");
                switch (strQue.Split('|')[1])
                {
                    case "OBRO":
                        li.Text = "Pc:" + strQue.Split('|')[2];
                        li.Tag = strQue.Split('|')[0].Trim();
                        li.ImageIndex = 1;
                        listView1.CheckBoxes = true;
                        trobat = false;
                        for (int i = 0; i < listView1.Items.Count; i++)
                        {
                            if (listView1.Items[i].Tag.ToString() == li.Tag.ToString())
                            {
                                trobat = true;
                                listView1.Items[i] = li;
                            }
                        }
                        if (!trobat) { listView1.Items.Add(li); }
                        //this.AddCheckBox(IPr.Address.ToString() + "|" + content.Split('|')[1]);
                        break;
                    case "USER":
                        li.Text = "Pc:" + strQue.Split('|')[2] + " Usuari:" + strQue.Split('|')[3];
                        li.Tag = strQue.Split('|')[0].Trim();
                        li.ImageIndex = 2;
                        listView1.CheckBoxes = true;
                        trobat = false;
                        for (int i = 0; i < listView1.Items.Count; i++)
                        {
                            if (listView1.Items[i].Tag.ToString() == li.Tag.ToString())
                            {
                                trobat = true;
                                listView1.Items[i] = li;
                            }
                        }
                        if (!trobat) { listView1.Items.Add(li); }
                        //this.AddCheckBox(IPr.Address.ToString() + "|" + content.Split('|')[1] + "|" + content.Split('|')[2]);
                        break;
                    case "SURTO":
                        li.Text = "Pc:" + strQue.Split('|')[2] + " Usuari:" + strQue.Split('|')[3];
                        li.Tag = strQue.Split('|')[0].Trim();
                        li.ImageIndex = 1;
                        listView1.CheckBoxes = true;
                        trobat = false;
                        for (int i = 0; i < listView1.Items.Count; i++)
                        {
                            if (listView1.Items[i].Tag.ToString() == li.Tag.ToString())
                            {
                                trobat = true;
                                listView1.Items[i] = li;
                            }
                        }
                        if (!trobat) { listView1.Items.Add(li); }
                        //this.AddCheckBox(IPr.Address.ToString() + "|" + content.Split('|')[1] + "|" + content.Split('|')[2]);
                        break;
                    case "APAGO":
                        li.Text = "Pc:" + strQue.Split('|')[2];
                        li.Tag = strQue.Split('|')[0].Trim();
                        li.ImageIndex = 0;
                        listView1.CheckBoxes = true;
                        trobat = false;
                        for (int i = 0; i < listView1.Items.Count; i++)
                        {
                            if (listView1.Items[i].Tag.ToString() == li.Tag.ToString())
                            {
                                trobat = true;
                                listView1.Items[i] = li;
                            }
                        }
                        if (!trobat) { listView1.Items.Add(li); }
                        //this.AddCheckBox(IPr.Address.ToString());
                        break;
                }
                //if (strQue.Split('|').Length > 2)
                //{
                //    li.Text = "Pc:" + strQue.Split('|')[1] +" Usuari:"+strQue.Split('|')[2];
                //    li.Tag = strQue.Split('|')[0];
                //    li.ImageIndex = 1;
                //    listView1.CheckBoxes = true;
                //    listView1.Items.Add(li);

                //}
                //else
                //{
                //    li.Text = "Pc:" + strQue.Split('|')[1];
                //    li.Tag = strQue.Split('|')[0];
                //    li.ImageIndex = 1;
                //    listView1.CheckBoxes = true;
                //    listView1.Items.Add(li);
                //}
               // this.checkedListBox1.Items.Add(strQue, true);
            }
        }

        private bool Ping(string server)
        {
            //Start ping

            //string server = "xxx.xxx.xxx.xxx";//address to verify, like 127.0.0.1
            bool trobat = false;
            IPAddress ipa = IPAddress.Parse(server);

            Ping p = new Ping();

            PingReply reply;

            reply = p.Send(server);
            if (reply.Address != null)
            {
                if (reply.Address.ToString() == ipa.ToString())
                {
                    trobat = true;
                }
            }
            /*
            int success = 0, insuccess = 0;

            for (int i = 0; i < 1; i++)
            {

                reply = p.Send(ipa);

                if (reply.Address == ipa)
                {

                    success++;
                    trobat = true;
                }
                else
                {
                    insuccess++;
                }

            }*/

//            MessageBox.Show("sent = 4, recived = " + success.ToString() + ", lost = " + insuccess.ToString() + " Server" + server.ToString());
            //Console.WriteLine("sent = 4, recived = {0}, lost = {1}", success, insuccess);

            //Console.ReadKey();
            return trobat;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //MessageBox.Show("Ha pasat 60 segons"+ DateTime.Now.ToShortDateString());
            //for (int i = 1; i < 254; i++)
            //{
            //    Ping("172.17.14." + i);
            //}
        }

        private void btnEnvia_Click(object sender, EventArgs e)
        {

            Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            for (int i = 0; i < this.listView1.Items.Count; i++)
            {
                if (this.listView1.Items[i].Checked)
                {
                    string resposta;
                    IPHostEntry address = Dns.GetHostEntry(this.listView1.Items[i].Tag.ToString());
                    IPEndPoint EP = new IPEndPoint(address.AddressList[0], 9999);
                    int bi;
                    try
                    {
                        socket.Connect(EP);
                        byte[] bytes = System.Text.Encoding.ASCII.GetBytes("MESSAGE");
                        socket.Send(bytes, bytes.Length, SocketFlags.None);
                        bytes = new byte[1024];
                        bi = socket.Receive(bytes, bytes.Length, SocketFlags.None);
                        resposta = Encoding.ASCII.GetString(bytes, 0, bi);

                        if (resposta == "REBUT")
                        {
                            //bytes = new byte[1024];
                            bytes = System.Text.Encoding.ASCII.GetBytes(this.textBox1.Text);
                            socket.Send(bytes, bytes.Length, SocketFlags.None);
                            socket.Disconnect(true);
                            socket.Shutdown(SocketShutdown.Both);
                            socket.Close();
                        }
                    }
                    catch
                    {
                       

                    }
                }
            }
            this.btnEnvia.Visible = false;
            this.textBox1.Visible = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
  
        }

         // Incoming data from client.
        public  string data = null;

        // Thread signal.
        public  ManualResetEvent allDone = new ManualResetEvent(false);

        public  void StartListening()
        {
            // Data buffer for incoming data.
            byte[] bytes = new Byte[1024];

            // Establish the local endpoint for the socket.
            // The DNS name of the computer
            // running the listener is "host.contoso.com".
            NetworkInterface[] ni = NetworkInterface.GetAllNetworkInterfaces();


            IPAddress ipAddress = Dns.GetHostEntry(ni[0].GetIPProperties().UnicastAddresses[0].Address.ToString()).AddressList[0];
            IPEndPoint localEndPoint = new IPEndPoint(ipAddress, 9999);

            // Create a TCP/IP socket.
            Socket listener = new Socket(AddressFamily.InterNetwork,
                SocketType.Stream, ProtocolType.Tcp);
            
            // Bind the socket to the local endpoint and listen for incoming connections.
            try
            {
                listener.Bind(localEndPoint);
                listener.Listen(100);

                while (true)
                {
                    // Set the event to nonsignaled state.
                    allDone.Reset();

                    // Start an asynchronous socket to listen for connections.
                    Console.WriteLine("Waiting for a connection...");
                    listener.BeginAccept(
                        new AsyncCallback(AcceptCallback),
                        listener);

                    // Wait until a connection is made before continuing.
                    allDone.WaitOne();
                }

            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }

            Console.WriteLine("\nPress ENTER to continue...");
            Console.Read();

        }

        public  void AcceptCallback(IAsyncResult ar)
        {
            // Signal the main thread to continue.
            allDone.Set();

            // Get the socket that handles the client request.
            Socket listener = (Socket)ar.AsyncState;
            Socket handler = listener.EndAccept(ar);

            // Create the state object.
            StateObject state = new StateObject();
            state.workSocket = handler;
            handler.BeginReceive(state.buffer, 0, StateObject.BufferSize, 0,
                new AsyncCallback(ReadCallback), state);
        }

        public  void ReadCallback(IAsyncResult ar)
        {
            String content = String.Empty;

            // Retrieve the state object and the handler socket
            // from the asynchronous state object.
            StateObject state = (StateObject)ar.AsyncState;
            Socket handler = state.workSocket;
            
            byte[] bytes = new byte[1024];
            int bytesRead = handler.EndReceive(ar);
            IPEndPoint IPr = (IPEndPoint)handler.RemoteEndPoint;
            
            
            if (bytesRead > 0)
            {
                content = Encoding.ASCII.GetString(state.buffer, 0, bytesRead);
                content = IPr.Address.ToString() + "|" + content;
                this.AddCheckBox(content);
               
                Send(handler, "quit");
                handler.Shutdown(SocketShutdown.Both);
                handler.Close();

                //if (content.IndexOf("\n") > -1)
                //{
                //    // All the data has been read from the 
                //    // client. Display it on the console.
                //    Console.WriteLine("Read {0} bytes from socket. \n Data : {1}",
                //        content.Length, content);
                //    // Echo the data back to the client.
                //    Send(handler, content);
                //}
                //else
                //{
                //    // Not all data received. Get more.
                //    handler.BeginReceive(state.buffer, 0, StateObject.BufferSize, 0,
                //    new AsyncCallback(ReadCallback), state);
                //}
            }
        }

        private  void Send(Socket handler, String data)
        {
            // Convert the string data to byte data using ASCII encoding.
            byte[] byteData = Encoding.ASCII.GetBytes(data);

            // Begin sending the data to the remote device.
            handler.BeginSend(byteData, 0, byteData.Length, 0,
                new AsyncCallback(SendCallback), handler);
        }

        private  void SendCallback(IAsyncResult ar)
        {
            try
            {
                // Retrieve the socket from the state object.
                Socket handler = (Socket)ar.AsyncState;

                // Complete sending the data to the remote device.
                int bytesSent = handler.EndSend(ar);
                Console.WriteLine("Sent {0} bytes to client.", bytesSent);

                // handler.Shutdown(SocketShutdown.Both);
                // handler.Close();

            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
    
        private void btnTerminal_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < this.listView1.CheckedItems.Count; i++)
            {
                //MessageBox.Show(System.Environment.CurrentDirectory + "\\plink.exe -i " + System.Environment.CurrentDirectory + "\\id_rsa.ppk root@" + this.listView1.CheckedItems[i].Tag.ToString() + " shutdown -h now");
                //System.Diagnostics.Process.Start(System.Environment.CurrentDirectory + "\\plink.exe", "-i " + System.Environment.CurrentDirectory + "\\id_rsa.ppk test@" + this.listView1.CheckedItems[i].Tag.ToString() + " sudo shutdown -h now");
                //MessageBox.Show(this.listView1.CheckedItems[i].Tag.ToString());
                string strSentencia = "";
                if (this.rdSurtSessio.Checked) {
                    Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                        if (this.listView1.Items[i].Checked)
                        {
                            string resposta;
                            IPHostEntry address = Dns.GetHostEntry(this.listView1.Items[i].Tag.ToString());
                            IPEndPoint EP = new IPEndPoint(address.AddressList[0], 9999);
                            int bi;
                            try
                            {
                                socket.Connect(EP);
                                byte[] bytes = System.Text.Encoding.ASCII.GetBytes("SURTSESSIO");
                                socket.Send(bytes, bytes.Length, SocketFlags.None);
                                bytes = new byte[1024];
                                bi = socket.Receive(bytes, bytes.Length, SocketFlags.None);
                                resposta = Encoding.ASCII.GetString(bytes, 0, bi);

                                if (resposta == "REBUT")
                                {
                                    //bytes = new byte[1024];
                                    bytes = System.Text.Encoding.ASCII.GetBytes(this.textBox1.Text);
                                    socket.Send(bytes, bytes.Length, SocketFlags.None);
                                    socket.Disconnect(true);
                                    socket.Shutdown(SocketShutdown.Both);
                                    socket.Close();
                                }
                            }
                            catch
                            {


                            }
                    }
                }
                else
                {
                    if (this.rdApaga.Checked)
                    {
                        strSentencia = "shutdown -h now";
                    }
                    if (this.rdReinicia.Checked)
                    {
                        strSentencia = "reboot";
                    }
                    System.Diagnostics.ProcessStartInfo pInfo = new System.Diagnostics.ProcessStartInfo(System.Environment.CurrentDirectory + "\\plink.exe", "-i \"" + System.Environment.CurrentDirectory + "\\id_rsa.ppk\" root@" + this.listView1.CheckedItems[i].Tag.ToString() + " " + strSentencia);
                    pInfo.RedirectStandardOutput = true;
                    //pInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden; // if you don’t want to see the application execute;
                    pInfo.UseShellExecute = false;

                    System.Diagnostics.Process listFiles;
                    listFiles = System.Diagnostics.Process.Start(pInfo);
                    System.IO.StreamReader processOutput = listFiles.StandardOutput;
                    listFiles.WaitForExit(2000);
                    if (listFiles.HasExited)
                    {
                        string processResults = processOutput.ReadToEnd();
                        MessageBox.Show(processResults);
                    }
                }
//                C:\Documents and Settings\espi\Mis documentos\Visual Studio 2005\Projects\Gestio
//Terminals\GestioTerminals\bin\Debug>plink.exe -i "c:\Documents and Settings\espi
//\Mis documentos\Visual Studio 2005\Projects\GestioTerminals\GestioTerminals\bin\
//Debug\id_rsa.ppk" root@172.17.14.18 shutdown -h now
            }
        }

        private void actualitzaScreenletToolStripMenuItem_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < this.listView1.CheckedItems.Count; i++)
            {

                string strSentencia = "/usr/share/local/telestany/updateScreenlet.sh";
                    System.Diagnostics.ProcessStartInfo pInfo = new System.Diagnostics.ProcessStartInfo(System.Environment.CurrentDirectory + "\\plink.exe", "-i \"" + System.Environment.CurrentDirectory + "\\id_rsa.ppk\" root@" + this.listView1.CheckedItems[i].Tag.ToString() + " " + strSentencia);
                    pInfo.RedirectStandardOutput = true;
                    //pInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden; // if you don’t want to see the application execute;
                    pInfo.UseShellExecute = false;

                    System.Diagnostics.Process listFiles;
                    listFiles = System.Diagnostics.Process.Start(pInfo);
                    System.IO.StreamReader processOutput = listFiles.StandardOutput;
                    listFiles.WaitForExit(2000);
                    if (listFiles.HasExited)
                    {
                        string processResults = processOutput.ReadToEnd();
                        MessageBox.Show(processResults);
                    }
            }

        }

        private void buscaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            for (int i = 100; i < 120; i++)
            {   
            string IpConsulta = "172.17.14." + i;

                if (Ping(IpConsulta))
                {
                    try
                    {

                            Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                            string resposta;
                            IPHostEntry address = Dns.GetHostEntry(IpConsulta); // Dns.GetHostEntry(this.listView1.Items[i].Tag.ToString());
                            IPEndPoint EP = new IPEndPoint(address.AddressList[0], 9998);
                            int bi;
                                socket.Connect(EP);
                                if (socket.Connected)
                                {
                                    byte[] bytes = System.Text.Encoding.ASCII.GetBytes("ONLINE");
                                    socket.Send(bytes, bytes.Length, SocketFlags.None);
                                    bytes = new byte[1024];
                                    bi = socket.Receive(bytes, bytes.Length, SocketFlags.None);
                                    resposta = Encoding.ASCII.GetString(bytes, 0, bi);
                                    ListViewItem li = new ListViewItem("pc");

                                    if (resposta.Split('|')[0] == "REBUT")
                                    {
                                        li.Text = "Pc:" + resposta.Split('|')[1];
                                        li.Tag = IpConsulta;
                                        li.ImageIndex = 2;
                                        listView1.CheckBoxes = true;
                                        bool trobat = false;
                                        for (int j = 0; j < listView1.Items.Count; j++)
                                        {
                                            if (listView1.Items[j].Tag.ToString() == li.Tag.ToString())
                                            {
                                                trobat = true;
                                                listView1.Items[j] = li;
                                            }
                                        }
                                        if (!trobat) { listView1.Items.Add(li); }

                                        //bytes = new byte[1024];
                                        // bytes = System.Text.Encoding.ASCII.GetBytes(this.textBox1.Text);
                                        // socket.Send(bytes, bytes.Length, SocketFlags.None);
                                        socket.Disconnect(true);
                                        socket.Shutdown(SocketShutdown.Both);
                                        socket.Close();
                                    }
                                }
                            }
                            catch
                            {
                            }
      
                }
            }
        }

        private void apagaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            EnviaaClient("SHUTDOWN");

        }

        private void enviaMissatgeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.textBox1.Visible = true;
            this.btnEnvia.Visible = true;

 
        }

        private void surtSessioToolStripMenuItem_Click(object sender, EventArgs e)
        {
            EnviaaClient("ENDSESSIO");
        }
        private void EnviaaClient(string Missatge)
        {
            for (int i = 0; i < this.listView1.CheckedItems.Count; i++)
            {
                Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                string resposta;
                IPHostEntry address = Dns.GetHostEntry(this.listView1.Items[i].Tag.ToString());
                IPEndPoint EP = new IPEndPoint(address.AddressList[0], 9998);
                int bi;
                try
                {
                    socket.Connect(EP);
                    byte[] bytes = System.Text.Encoding.ASCII.GetBytes(Missatge);
                    socket.Send(bytes, bytes.Length, SocketFlags.None);
                    bytes = new byte[1024];
                    bi = socket.Receive(bytes, bytes.Length, SocketFlags.None);
                    resposta = Encoding.ASCII.GetString(bytes, 0, bi);
                    resposta = resposta.Split('|')[0];
                    if (resposta == "REBUT")
                    {
                        //bytes = new byte[1024];
                       // bytes = System.Text.Encoding.ASCII.GetBytes(this.textBox1.Text);
                       // socket.Send(bytes, bytes.Length, SocketFlags.None);
                        socket.Disconnect(true);
                        socket.Shutdown(SocketShutdown.Both);
                        socket.Close();
                    }
                }
                catch
                {


                }
            }
        }

        private void reiniciaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            EnviaaClient("REBOOT");
        }

        private void updateUsersToolStripMenuItem_Click(object sender, EventArgs e)
        {
            EnviaaClient("UPDATEUSERS");
        }
    }
    public class StateObject
    {
        // Client  socket.
        public Socket workSocket = null;
        // Size of receive buffer.
        public const int BufferSize = 1024;
        // Receive buffer.
        public byte[] buffer = new byte[BufferSize];
        // Received data string.
        public StringBuilder sb = new StringBuilder();

    }

    public class AsynchronousSocketListener
    {


    }


}