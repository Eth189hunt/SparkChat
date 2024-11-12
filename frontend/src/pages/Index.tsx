import { useState } from "react";
import ServerList from "../components/ServerList";
import ChannelList from "../components/ChannelList";
import ChatArea from "../components/ChatArea";

const Index = () => {
  const [selectedChannel, setSelectedChannel] = useState("general");

  return (
    <div className="flex h-screen">
      <ServerList />
      <ChannelList selectedChannel={selectedChannel} onChannelSelect={setSelectedChannel} />
      <ChatArea selectedChannel={selectedChannel} />
    </div>
  );
};

export default Index;