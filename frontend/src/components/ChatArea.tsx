import { Send, Hash } from "lucide-react";
import { useState } from "react";
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuTrigger,
} from "@/components/ui/context-menu";

interface Message {
  id: number;
  user: string;
  content: string;
  timestamp: string;
  channelId: string;
}

interface ChatAreaProps {
  selectedChannel: string;
}

const ChatArea = ({ selectedChannel }: ChatAreaProps) => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      user: "User",
      content: "Welcome to SparkChat! 🎉",
      timestamp: "Today at 12:00 PM",
      channelId: "general"
    }
  ]);

  const [newMessage, setNewMessage] = useState("");

  const handleDeleteMessage = (id: number) => {
    setMessages(messages.filter(msg => msg.id !== id));
  };

  const handleSendMessage = () => {
    if (newMessage.trim()) {
      setMessages([
        ...messages,
        {
          id: Date.now(),
          user: "User",
          content: newMessage.trim(),
          timestamp: new Date().toLocaleTimeString(),
          channelId: selectedChannel
        }
      ]);
      setNewMessage("");
    }
  };

  // Filter messages for the current channel
  const channelMessages = messages.filter(msg => msg.channelId === selectedChannel);

  return (
    <div className="flex-1 flex flex-col bg-[#36393f]">
      <div className="h-12 border-b border-discord-dark/50 flex items-center px-4">
        <Hash className="w-5 h-5 text-discord-light mr-2" />
        <h2 className="text-white font-semibold">{selectedChannel}</h2>
      </div>
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {channelMessages.map((message) => (
          <ContextMenu key={message.id}>
            <ContextMenuTrigger>
              <div className="flex items-start gap-4">
                <div className="w-10 h-10 rounded-full bg-discord-primary flex-shrink-0"></div>
                <div>
                  <div className="flex items-center gap-2">
                    <span className="text-white font-medium">{message.user}</span>
                    <span className="text-discord-light text-xs">{message.timestamp}</span>
                  </div>
                  <p className="text-discord-light">{message.content}</p>
                </div>
              </div>
            </ContextMenuTrigger>
            <ContextMenuContent>
              <ContextMenuItem onClick={() => handleDeleteMessage(message.id)}>
                Delete Message
              </ContextMenuItem>
            </ContextMenuContent>
          </ContextMenu>
        ))}
      </div>
      <div className="p-4">
        <div className="bg-[#40444b] rounded-lg flex items-center p-4 gap-4">
          <input
            type="text"
            value={newMessage}
            onChange={(e) => setNewMessage(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                handleSendMessage();
              }
            }}
            placeholder={`Message #${selectedChannel}`}
            className="bg-transparent flex-1 text-discord-light focus:outline-none placeholder:text-discord-light"
          />
          <Send 
            className="w-6 h-6 text-discord-light cursor-pointer hover:text-white transition-colors"
            onClick={handleSendMessage}
          />
        </div>
      </div>
    </div>
  );
};

export default ChatArea;