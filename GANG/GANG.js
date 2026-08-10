export async function GANG() {

  const folders = [
    "GANG",
    "HESS",
    "eco",
    "expand",
    "grid",
    "link",
    "dezi"
  ];

  const system = {
    root: null,
    chain: [],
    errors: [],
    status: "INIT"
  };

  // ROOT laden
  try {
    const root = await import("./GANG.root.js");
    system.root = root.ROOT || "NO_ROOT";
  } catch (err) {
    system.errors.push("ROOT fehlt: " + err);
  }

  // Ordner laden
  for (const folder of folders) {
    try {
      const mod = await import(`./${folder}/agent.js`);
      system.chain.push({
        folder,
        status: "OK",
        agent: mod.agent || "NO_AGENT"
      });
    } catch (err) {
      system.chain.push({
        folder,
        status: "ERR",
        agent: null
      });
      system.errors.push(`Fehler in ${folder}/agent.js: ${err}`);
    }
  }

  system.status = system.errors.length === 0 ? "OK" : "WARN";

  return system;
}
