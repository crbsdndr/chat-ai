import Image from "next/image";


export default function ChatIDLayout({
  children
}: Readonly<{
  children: React.ReactNode
}>
) {
  return (
      <main className="w-full flex flex-1 flex-col bg-amber-500 ">
        <header className="h-1/15 flex justify-center items-center bg-black">
          <h2 className="text-amber-500">User</h2>
        </header>
        <div className="h-full flex flex-col p-2">
          {children}
        </div>
        <form className="w-full flex flex-row bg-black h-1/12 p-2 items-center gap-2">
          <textarea className="w-full h-11/12 border-2 border-amber-500 rounded-2xl indent-2 outline-0" id="message" name="message" placeholder="Ketik pesan..."></textarea>
          <button type="submit" className="relative w-10 h-10">
            <Image
              src="/send.svg"
              alt="Send Message"
              fill
            />
          </button>
        </form>
      </main>
  )
}