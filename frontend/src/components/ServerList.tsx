import { Home, Plus, Trash2 } from "lucide-react";
import { useState } from "react";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

const ServerList = () => {
  const [servers, setServers] = useState<string[]>([]);
  const [newServer, setNewServer] = useState("");

  const handleAddServer = (e: React.FormEvent) => {
    e.preventDefault();
    if (newServer.trim()) {
      setServers([...servers, newServer.trim()]);
      setNewServer("");
    }
  };

  const handleDeleteServer = (serverName: string) => {
    setServers(servers.filter(server => server !== serverName));
  };

  return (
    <div className="w-20 bg-discord-dark flex flex-col items-center py-4 gap-4">
      <div className="w-12 h-12 bg-discord-primary rounded-2xl flex items-center justify-center hover:bg-discord-secondary hover:rounded-xl transition-all duration-200 cursor-pointer">
        <Home className="w-6 h-6 text-white" />
      </div>
      <div className="w-12 h-0.5 bg-discord-light/20 rounded-full" />
      
      {servers.map((server) => (
        <div key={server} className="relative group">
          <div className="w-12 h-12 bg-discord-primary rounded-2xl flex items-center justify-center hover:bg-discord-secondary hover:rounded-xl transition-all duration-200 cursor-pointer">
            {server[0].toUpperCase()}
          </div>
          <button
            onClick={() => handleDeleteServer(server)}
            className="absolute -right-2 -top-2 bg-red-500 rounded-full p-1 hidden group-hover:block hover:bg-red-600"
          >
            <Trash2 className="w-3 h-3 text-white" />
          </button>
        </div>
      ))}

      <Dialog>
        <DialogTrigger asChild>
          <div className="w-12 h-12 bg-discord-dark rounded-2xl flex items-center justify-center hover:bg-discord-secondary hover:rounded-xl transition-all duration-200 cursor-pointer border-2 border-discord-light/20">
            <Plus className="w-6 h-6 text-discord-light" />
          </div>
        </DialogTrigger>
        <DialogContent className="bg-discord-dark border-none text-white">
          <DialogHeader>
            <DialogTitle>Add New Server</DialogTitle>
          </DialogHeader>
          <form onSubmit={handleAddServer} className="space-y-4">
            <Input
              type="text"
              value={newServer}
              onChange={(e) => setNewServer(e.target.value)}
              placeholder="Enter server name"
              className="bg-[#40444b] border-none text-white"
            />
            <Button type="submit" className="w-full">
              Add Server
            </Button>
          </form>
        </DialogContent>
      </Dialog>
    </div>
  );
};

export default ServerList;