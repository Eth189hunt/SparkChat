import { Hash, Plus } from "lucide-react";
import { useState } from "react";
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuTrigger,
} from "@/components/ui/context-menu";

interface ChannelListProps {
  selectedChannel: string;
  onChannelSelect: (channel: string) => void;
}

const ChannelList = ({ selectedChannel, onChannelSelect }: ChannelListProps) => {
  const [showNameInput, setShowNameInput] = useState(false);
  const [newUsername, setNewUsername] = useState("");
  const [username, setUsername] = useState("User");
  const [channels, setChannels] = useState(["general", "random"]);
  const [showChannelInput, setShowChannelInput] = useState(false);
  const [newChannel, setNewChannel] = useState("");
  const [editingChannel, setEditingChannel] = useState("");
  const [newChannelName, setNewChannelName] = useState("");

  const handleUsernameChange = () => {
    if (newUsername.trim()) {
      setUsername(newUsername);
      setNewUsername("");
      setShowNameInput(false);
    }
  };

  const handleAddChannel = () => {
    if (newChannel.trim() && !channels.includes(newChannel.trim())) {
      setChannels([...channels, newChannel.trim()]);
      setNewChannel("");
      setShowChannelInput(false);
    }
  };

  const handleDeleteChannel = (channel: string) => {
    if (channel !== "general") {
      setChannels(channels.filter((c) => c !== channel));
      if (selectedChannel === channel) {
        onChannelSelect("general");
      }
    }
  };

  const handleRenameChannel = (channel: string, newName: string) => {
    if (channel !== "general" && newName.trim() && !channels.includes(newName.trim())) {
      setChannels(channels.map((c) => (c === channel ? newName.trim() : c)));
      if (selectedChannel === channel) {
        onChannelSelect(newName.trim());
      }
      setEditingChannel("");
      setNewChannelName("");
    }
  };

  return (
    <div className="w-60 bg-[#2f3136] flex flex-col">
      <div className="h-12 border-b border-discord-dark/50 flex items-center px-4">
        <h2 className="text-white font-semibold">SparkChat</h2>
      </div>
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        <div>
          <div className="flex items-center justify-between mb-2">
            <h3 className="text-discord-light uppercase text-xs font-semibold">Text Channels</h3>
            <Plus 
              className="w-4 h-4 text-discord-light cursor-pointer hover:text-white transition-colors"
              onClick={() => setShowChannelInput(!showChannelInput)}
            />
          </div>
          {showChannelInput && (
            <div className="mb-2">
              <input
                type="text"
                value={newChannel}
                onChange={(e) => setNewChannel(e.target.value)}
                placeholder="New channel name"
                className="bg-[#40444b] text-white px-3 py-2 rounded-md w-full focus:outline-none text-sm mb-2"
              />
              <button
                onClick={handleAddChannel}
                className="bg-discord-primary text-white px-3 py-1 rounded-md w-full hover:bg-discord-secondary transition-colors text-sm"
              >
                Add Channel
              </button>
            </div>
          )}
          <div className="space-y-1">
            {channels.map((channel) => (
              <ContextMenu key={channel}>
                <ContextMenuTrigger>
                  <div 
                    className={`flex items-center gap-2 text-discord-light hover:bg-discord-dark rounded p-2 cursor-pointer group ${
                      selectedChannel === channel ? "bg-discord-dark text-white" : ""
                    }`}
                    onClick={() => onChannelSelect(channel)}
                  >
                    <Hash className="w-5 h-5" />
                    {editingChannel === channel ? (
                      <input
                        type="text"
                        value={newChannelName}
                        onChange={(e) => setNewChannelName(e.target.value)}
                        onKeyDown={(e) => {
                          if (e.key === "Enter") {
                            handleRenameChannel(channel, newChannelName);
                          }
                        }}
                        className="bg-[#40444b] text-white px-2 py-1 rounded-md focus:outline-none text-sm"
                        autoFocus
                      />
                    ) : (
                      <span className="group-hover:text-white transition-colors">{channel}</span>
                    )}
                  </div>
                </ContextMenuTrigger>
                <ContextMenuContent>
                  {channel !== "general" && (
                    <>
                      <ContextMenuItem
                        onClick={() => {
                          setEditingChannel(channel);
                          setNewChannelName(channel);
                        }}
                      >
                        Rename
                      </ContextMenuItem>
                      <ContextMenuItem onClick={() => handleDeleteChannel(channel)}>
                        Delete
                      </ContextMenuItem>
                    </>
                  )}
                </ContextMenuContent>
              </ContextMenu>
            ))}
          </div>
        </div>
      </div>
      <div className="h-14 bg-[#292b2f] px-4 flex items-center">
        <div 
          className="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity"
          onClick={() => setShowNameInput(!showNameInput)}
        >
          <div className="w-8 h-8 rounded-full bg-discord-primary"></div>
          <div className="text-white text-sm font-medium">{username}</div>
        </div>
        {showNameInput && (
          <div className="absolute bottom-16 left-4 bg-discord-dark p-4 rounded-lg shadow-lg">
            <input
              type="text"
              value={newUsername}
              onChange={(e) => setNewUsername(e.target.value)}
              placeholder="New username"
              className="bg-[#40444b] text-white px-3 py-2 rounded-md mb-2 w-full focus:outline-none"
            />
            <button
              onClick={handleUsernameChange}
              className="bg-discord-primary text-white px-4 py-2 rounded-md w-full hover:bg-discord-secondary transition-colors"
            >
              Change Username
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default ChannelList;